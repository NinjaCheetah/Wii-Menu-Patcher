import sys
import os
import zipfile
import tarfile
import urllib.request

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from qt.py.ui_MainMenu import Ui_MainWindow

wadPath = ""
wadName = ""
toolsDir = os.path.join(os.getcwd(), "tools")


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.exit_btn.clicked.connect(self.exit_btn_pressed)
        self.ui.selectWAD_btn.clicked.connect(self.selectWAD_btn_pressed)
        self.ui.downloadTools_btn.clicked.connect(self.downloadTools_btn_pressed)
        if os.path.exists(toolsDir):
            if os.path.exists(os.path.join(toolsDir, "Sharpii.exe")) and os.path.exists(os.path.join(toolsDir, "ASH")) and os.path.exists(os.path.join(toolsDir, "ashcompress.exe")):
                self.ui.status_lbl.setText("Ready. (Tools Ready)")
                self.ui.extract_btn.setEnabled(True)
                self.ui.pack_btn.setEnabled(True)
                self.ui.cleanUp_btn.setEnabled(True)

    def downloadTools_btn_pressed(self):
        self.ui.status_lbl.setText("Downloading tools...")
        self.ui.status_lbl.repaint()
        global toolsDir
        print("WAD is set to: {}, located at path: {}".format(wadName, wadPath))
        print(toolsDir)
        if not os.path.exists(toolsDir):
            os.makedirs(toolsDir)
        # Download Sharpii
        urllib.request.urlretrieve(
            "https://github.com/mogzol/sharpii/releases/latest/download/Sharpii_v1.7.3.zip",
            os.path.join(toolsDir, "Sharpii.zip"))
        with zipfile.ZipFile(os.path.join(toolsDir, "Sharpii.zip"), "r") as zip_ref:
            zip_ref.extractall(toolsDir)
        os.remove(os.path.join(toolsDir, "Sharpii.zip"))
        print("Sharpii is ready at {}".format(os.path.join(toolsDir, "Sharpii.exe")))
        # Download ASH
        urllib.request.urlretrieve(
            "https://github.com/NinjaCheetah/ASH_Extractor/releases/latest/download/ASH-Linux.tar",
            os.path.join(toolsDir, "ASH-Linux.tar"))
        with tarfile.TarFile(os.path.join(toolsDir, "ASH-Linux.tar"), "r") as tar_ref:
            tar_ref.extractall(toolsDir)
        os.remove(os.path.join(toolsDir, "ASH-Linux.tar"))
        print("ASH is ready at {}".format(os.path.join(toolsDir, "ASH")))
        # Download ASHcompress
        urllib.request.urlretrieve(
            "https://gbatemp.net/download/ash-compressor.34055/download",
            os.path.join(toolsDir, "ASHcompress.zip"))
        with zipfile.ZipFile(os.path.join(toolsDir, "ASHcompress.zip"), "r") as zip_ref:
            zip_ref.extractall(toolsDir)
        os.remove(os.path.join(toolsDir, "ASHcompress.zip"))
        print("ASHcompress ready at {}".format(os.path.join(toolsDir, "ashcompress.exe")))
        # Tools are now ready!
        print("Tools ready! Unlocking UI")
        self.ui.status_lbl.setText("Ready. (Tools Ready)")
        self.ui.extract_btn.setEnabled(True)
        self.ui.pack_btn.setEnabled(True)
        self.ui.cleanUp_btn.setEnabled(True)

    def selectWAD_btn_pressed(self):
        inc_filePath = QFileDialog.getOpenFileName(self, "Open WAD", "", "WAD File (*.wad)")
        if inc_filePath[0] != "":
            global wadPath
            wadPath = inc_filePath[0]
            global wadName
            wadName = os.path.basename(wadPath).split('/')[-1]
            self.ui.selectWAD_btn.setText(wadName)

    def exit_btn_pressed(self):
        sys.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
