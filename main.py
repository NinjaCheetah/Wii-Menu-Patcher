import sys
import os
import zipfile
import tarfile
import subprocess
from urllib.request import urlopen

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtCore import QCoreApplication

from qt.py.ui_MainMenu import Ui_MainWindow

wadPath = ""
wadName = ""
toolsDir = os.path.join(os.getcwd(), "tools")


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.downloader = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.progressBar.hide()
        self.ui.exit_btn.clicked.connect(self.exit_btn_pressed)
        self.ui.selectWAD_btn.clicked.connect(self.selectWAD_btn_pressed)
        self.ui.downloadTools_btn.clicked.connect(self.downloadTools_btn_pressed)
        self.ui.extract_btn.clicked.connect(self.extract_btn_pressed)
        if os.path.exists(toolsDir):
            if os.path.exists(os.path.join(toolsDir, "Sharpii.exe")) and os.path.exists(os.path.join(toolsDir, "ASH")) and os.path.exists(os.path.join(toolsDir, "ashcompress.exe")):
                self.ui.status_lbl.setText("Ready. (Tools Ready)")
                self.ui.extract_btn.setEnabled(True)
                self.ui.pack_btn.setEnabled(True)
                self.ui.cleanUp_btn.setEnabled(True)

    def downloadTools_btn_pressed(self):
        self.ui.status_lbl.setText("Downloading tools...")
        self.ui.downloadTools_btn.setEnabled(False)
        self.ui.extract_btn.setEnabled(False)
        self.ui.pack_btn.setEnabled(False)
        self.ui.cleanUp_btn.setEnabled(False)
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
        for item in toolsToDownload:
            readBytes = 0
            with urlopen(item[0]) as r:
                self.ui.progressBar.setMaximum(int(r.info()["Content-Length"]))
                with open(os.path.join(toolsDir, item[1]), "ab") as f:
                    while True:
                        QCoreApplication.processEvents()
                        chunk = r.read(128)
                        if chunk is None:
                            continue
                        elif chunk == b"":
                            break
                        f.write(chunk)
                        readBytes += 128
                        self.ui.progressBar.setValue(readBytes)
            print("Downloaded file {} to {}".format(item[0], item[1]))
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
        self.ui.status_lbl.setText("Ready. (Tools Ready)")
        self.ui.progressBar.hide()
        self.ui.downloadTools_btn.setEnabled(True)
        self.ui.extract_btn.setEnabled(True)
        self.ui.pack_btn.setEnabled(True)
        self.ui.cleanUp_btn.setEnabled(True)

    def extract_btn_pressed(self):
        if wadPath == "":
            msgBox = QMessageBox()
            msgBox.setText("Please select a WAD first.")
            msgBox.exec()
        else:
            if os.path.exists("wad"):
                msgBox = QMessageBox()
                msgBox.setText("WAD has already been extracted!")
                msgBox.exec()
            else:
                process = subprocess.run(['wine', os.path.join(toolsDir, "Sharpii.exe"), 'WAD', '-u', wadPath, 'wad/'])
                process = subprocess.run(['wine', os.path.join(toolsDir, "Sharpii.exe"),
                                          'U8', '-u', 'wad/00000001.app', '00000001/'])
                os.rename("00000001/layout/common/diskBann.ash", "diskBann.ash")
                process = subprocess.run([os.path.join(toolsDir, "ASH"), 'diskBann.ash'])
                process = subprocess.run(['wine', os.path.join(toolsDir, "Sharpii.exe"),
                                          'U8', '-u', 'diskBann.ash.arc', 'diskBann/'])
                os.remove("diskBann.ash")
                os.remove("diskBann.ash.arc")

    def selectWAD_btn_pressed(self):
        inc_filePath = QFileDialog.getOpenFileName(self, "Open WAD", "", "WAD File (*.wad)")
        if inc_filePath[0] != "":
            global wadPath
            wadPath = inc_filePath[0]
            global wadName
            wadName = os.path.basename(wadPath).split('/')[-1]
            self.ui.selectWAD_btn.setText(wadName)

    def exit_btn_pressed(self):
        app.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
