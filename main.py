import sys
import os
import zipfile
import tarfile
import hashlib
import asyncio
from urllib.request import urlopen

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QCoreApplication, QThread, Signal

from qt.py.ui_newui import Ui_MainWindow

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
        for file in self._files:
            readBytes = 0
            chunkSize = 1024

            self.setCurrentProgress.emit(0)
            with urlopen(file[0]) as r:
                self.setTotalProgress.emit(int(r.info()["Content-Length"]))
                with open(os.path.join(toolsDir, file[1]), "ab") as f:
                    while True:
                        chunk = r.read(chunkSize)
                        if chunk is None:
                            continue
                        elif chunk == b"":
                            break
                        f.write(chunk)
                        readBytes += chunkSize
                        self.setCurrentProgress.emit(readBytes)
                print("Downloaded file {}".format(file[1]))


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
        self.ui.status_lbl.setText("Downloading tools...")
        self.ui.downloadTools_btn.setEnabled(False)
        self.ui.progressBar.show()
        global toolsDir
        print("WAD is set to: {}, located at path: {}".format(wadName, wadPath))
        print(toolsDir)
        if not os.path.exists(toolsDir):
            os.makedirs(toolsDir)
        toolsToDownload = [
            ("https://github.com/mogzol/sharpii/releases/latest/download/Sharpii_v1.7.3.zip", "Sharpii.zip"),
            ("https://github.com/NinjaCheetah/ASH_Extractor/releases/latest/download/ASH-Linux.tar", "ASH-Linux.tar"),
            ("https://github.com/NinjaCheetah/ASH_Extractor/releases/latest/download/ashcompress.zip", "ashcompress.zip")
        ]
        self.downloader = Downloader(toolsToDownload)
        self.downloader.setTotalProgress.connect(self.ui.progressBar.setMaximum)
        self.downloader.setCurrentProgress.connect(self.ui.progressBar.setValue)
        self.downloader.finished.connect(self.downloadFinished)
        self.downloader.start()

    def downloadFinished(self):
        self.ui.progressBar.setValue(self.ui.progressBar.maximum())
        with zipfile.ZipFile(os.path.join(toolsDir, "Sharpii.zip"), "r") as zip_ref:
            zip_ref.extractall(toolsDir)
        os.remove(os.path.join(toolsDir, "Sharpii.zip"))
        print("Sharpii is ready at {}".format(os.path.join(toolsDir, "Sharpii.exe")))
        with tarfile.TarFile(os.path.join(toolsDir, "ASH-Linux.tar"), "r") as tar_ref:
            tar_ref.extractall(toolsDir)
        os.remove(os.path.join(toolsDir, "ASH-Linux.tar"))
        print("ASH is ready at {}".format(os.path.join(toolsDir, "ASH")))
        with zipfile.ZipFile(os.path.join(toolsDir, "ashcompress.zip"), "r") as zip_ref:
            zip_ref.extractall(toolsDir)
        os.remove(os.path.join(toolsDir, "ashcompress.zip"))
        print("ASHcompress ready at {}".format(os.path.join(toolsDir, "ashcompress.exe")))
        # Tools are now ready!
        print("Tools ready! Unlocking UI")
        self.ui.status_lbl.setText("Ready.")
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
            with open(wadPath, 'rb', buffering=0) as f:
                wadHash = hashlib.file_digest(f, 'md5').hexdigest()
            wadVersion = getMenuVersionCode(wadHash)
            wadRegion = getMenuRegionCode(wadHash)
            if wadVersion != "Unknown Version":
                self.ui.WADstatus_lbl.setText(f"**WAD selected:** {wadName} <br />"
                                              f"**Identified version:** {wadVersion} <br />"
                                              f"**Identified region:** {wadRegion}")
            else:
                self.ui.WADstatus_lbl.setText(f"**WAD selected:** {wadName} <br />"
                                              f"**Identified version:** Unknown version! <br />"
                                              f"**Identified region:** Unknown region!")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
