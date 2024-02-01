import json

from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import QCoreApplication, QThread, Signal

from qt.py.ui_Patch import Ui_Patch


class PatchTab(QWidget, Ui_Patch):
    def __init__(self):
        super(PatchTab, self).__init__()
        self.ui = Ui_Patch()
        self.ui.setupUi(self)
        with open("cache.json", "r") as file:
            self.cache = json.load(file)
        self.ui.wadInfo_lbl.setText("**Identified version:** {} <br />"
                                    "**Identified region:** {}"
                                    .format(self.cache["version"], self.cache["region"]))
