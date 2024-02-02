import sys
import os
import zipfile
import tarfile
import hashlib
import pathlib
import json
import urllib3

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtCore import QThread, Signal, Qt

from qt.py.ui_MainMenu import Ui_MainWindow
from tabs.patch import PatchTab

from data.sysMenuVersions import getMenuVersionCode, getMenuRegionCode
from plat.prepareTools import getToolsIndex

wadPath = ""
wadName = ""
toolsDir = os.path.join(os.getcwd(), "tools")


class Downloader(QThread):

    setTotalProgress = Signal(int)
    setCurrentProgress = Signal(int)

    def __init__(self, files):
        super().__init__()
        self._files = files

    def run(self):
        http = urllib3.PoolManager()

        for file in self._files:
            readBytes = 0
            chunkSize = 1024

            self.setCurrentProgress.emit(0)
            r = http.request('GET', file[0], preload_content=False)
            self.setTotalProgress.emit(int(r.info()["Content-Length"]))

            with open(os.path.join(toolsDir, file[1]), 'wb') as out:
                while True:
                    data = r.read(chunkSize)
                    if not data:
                        break
                    out.write(data)
                    readBytes += chunkSize
                    self.setCurrentProgress.emit(readBytes)
                print("Downloaded file {}".format(file[1]))

            r.release_conn()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.downloader = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.progressBar.hide()
        self.ui.selectWAD_btn.clicked.connect(self.selectWAD_btn_pressed)
        self.ui.downloadTools_btn.clicked.connect(self.downloadTools_btn_pressed)
        if os.path.exists(toolsDir):
            if os.path.exists(os.path.join(toolsDir, "Sharpii.exe")) and os.path.exists(os.path.join(toolsDir, "ASH")) and os.path.exists(os.path.join(toolsDir, "ashcompress.exe")):
                self.ui.status_lbl.setText("Ready.")
                self.ui.toolStatus_lbl.setText("Tools ready!")

    def downloadTools_btn_pressed(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Confirm Tools Download")
        msgBox.setIcon(QMessageBox.Icon.Information)
        msgBox.setTextFormat(Qt.MarkdownText)
        msgBox.setText("### This will download the following external tools required for this program.")
        msgBox.setInformativeText("These programs are all safe to use, however you may inspect where they originate from using the links below if you would prefer to do so. <br /><br />"
                                  "Sharpii: <a href='https://github.com/mogzol/sharpii'>GitHub Repository</a> <br />"
                                  "ASH: <a href='https://github.com/NinjaCheetah/ASH_Extractor'>GitHub Repository</a> <br />"
                                  "ashcompress: <a href='https://gbatemp.net/download/ash-compressor.34055/'>GBATemp</a> <br")
        msgBox.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        msgBox.setDefaultButton(QMessageBox.StandardButton.Ok)
        ret = msgBox.exec()
        if ret == QMessageBox.StandardButton.Ok:
            self.ui.status_lbl.setText("Downloading tools...")
            self.ui.downloadTools_btn.setEnabled(False)
            self.ui.progressBar.show()
            global toolsDir
            if not os.path.exists(toolsDir):
                os.makedirs(toolsDir)
            toolsToDownload = getToolsIndex()
            self.downloader = Downloader(toolsToDownload)
            self.downloader.setTotalProgress.connect(self.ui.progressBar.setMaximum)
            self.downloader.setCurrentProgress.connect(self.ui.progressBar.setValue)
            self.downloader.finished.connect(self.downloadFinished)
            self.downloader.start()
        elif ret == QMessageBox.StandardButton.Cancel:
            return

    def downloadFinished(self):
        self.ui.progressBar.setValue(self.ui.progressBar.maximum())
        toolsList = getToolsIndex()
        for tool in toolsList:
            if pathlib.Path(tool[1]).suffix == ".zip":
                with zipfile.ZipFile(os.path.join(toolsDir, tool[1])) as fileToUnzip:
                    fileToUnzip.extractall(toolsDir)
            elif pathlib.Path(tool[1]).suffix == ".tar":
                with tarfile.TarFile(os.path.join(toolsDir, tool[1])) as fileToUntar:
                    fileToUntar.extractall(toolsDir)
            os.remove(os.path.join(toolsDir, tool[1]))
            print("Unzipped tool: {}".format(tool[1]))
        # Tools are now ready!
        self.ui.toolStatus_lbl.setText("Tools ready!")
        self.ui.progressBar.hide()
        self.ui.downloadTools_btn.setEnabled(True)
        self.ui.status_lbl.setText("Ready.")
        del self.downloader

    def selectWAD_btn_pressed(self):
        inc_filePath = QFileDialog.getOpenFileName(self, "Open WAD", "", "WAD File (*.wad)")
        if inc_filePath[0] != "":
            global wadPath
            wadPath = inc_filePath[0]
            global wadName
            wadName = os.path.basename(wadPath).split('/')[-1]
            wadData = {"version": "", "region": "", "hash": ""}
            with open(wadPath, 'rb', buffering=0) as f:
                wadData["hash"] = hashlib.file_digest(f, 'md5').hexdigest()
            wadData["version"] = getMenuVersionCode(wadData["hash"])
            wadData["region"] = getMenuRegionCode(wadData["hash"])
            with open("cache.json", 'w', encoding='utf-8') as file:
                json.dump(wadData, file, ensure_ascii=False)
            if self.ui.tabWidget.count() > 1:
                for tab in range(1, self.ui.tabWidget.count()):
                    self.ui.tabWidget.removeTab(tab)
            self.ui.tabWidget.addTab(PatchTab(), "Patch")
            if wadData["version"] != "Unknown Version":
                self.ui.WADstatus_lbl.setText("**WAD selected:** {} <br />"
                                              "**Identified version:** {} <br />"
                                              "**Identified region:** {}"
                                              .format(wadName, wadData["version"], wadData["region"]))
                msgBox = QMessageBox()
                msgBox.setWindowTitle("Ready for Patching")
                msgBox.setIcon(QMessageBox.Icon.Information)
                msgBox.setTextFormat(Qt.MarkdownText)
                msgBox.setText("### WAD loaded successfully!")
                msgBox.setInformativeText("You may now apply patches using the \"Patch\" tab.")
                msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
                msgBox.setDefaultButton(QMessageBox.StandardButton.Ok)
                msgBox.exec()
            else:
                self.ui.WADstatus_lbl.setText(f"**WAD selected:** {wadName} <br />"
                                              f"**Identified version:** Unknown version! <br />"
                                              f"**Identified region:** Unknown region!")
                msgBox = QMessageBox()
                msgBox.setWindowTitle("WAD Not Recognized")
                msgBox.setIcon(QMessageBox.Icon.Warning)
                msgBox.setTextFormat(Qt.MarkdownText)
                msgBox.setText("### The WAD you provided could not be recognized!")
                msgBox.setInformativeText("You may still attempt to apply patches using the \"Patch\" tab, however some patches may not work as expected. <br /> <br />"
                                          "Please be careful when using any WADs created from the WAD provided, as incorrectly applied patches could prevent the system from booting.")
                msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
                msgBox.setDefaultButton(QMessageBox.StandardButton.Ok)
                msgBox.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    if os.path.exists("cache.json"):
        os.remove("cache.json")

    sys.exit(app.exec())
