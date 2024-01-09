# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainMenu.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(680, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Sans Serif"])
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Sans Serif"])
        font1.setPointSize(16)
        self.label.setFont(font1)

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_2.addWidget(self.label_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.selectWAD_btn = QPushButton(self.centralwidget)
        self.selectWAD_btn.setObjectName(u"selectWAD_btn")

        self.horizontalLayout.addWidget(self.selectWAD_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.cleanUp_btn = QPushButton(self.centralwidget)
        self.cleanUp_btn.setObjectName(u"cleanUp_btn")
        self.cleanUp_btn.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cleanUp_btn.sizePolicy().hasHeightForWidth())
        self.cleanUp_btn.setSizePolicy(sizePolicy1)
        self.cleanUp_btn.setFont(font)
        icon = QIcon(QIcon.fromTheme(u"edit-delete"))
        self.cleanUp_btn.setIcon(icon)

        self.gridLayout.addWidget(self.cleanUp_btn, 1, 1, 1, 1)

        self.extract_btn = QPushButton(self.centralwidget)
        self.extract_btn.setObjectName(u"extract_btn")
        self.extract_btn.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.extract_btn.sizePolicy().hasHeightForWidth())
        self.extract_btn.setSizePolicy(sizePolicy1)
        self.extract_btn.setFont(font)
        icon1 = QIcon(QIcon.fromTheme(u"document-open"))
        self.extract_btn.setIcon(icon1)

        self.gridLayout.addWidget(self.extract_btn, 0, 1, 1, 1)

        self.downloadTools_btn = QPushButton(self.centralwidget)
        self.downloadTools_btn.setObjectName(u"downloadTools_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.downloadTools_btn.sizePolicy().hasHeightForWidth())
        self.downloadTools_btn.setSizePolicy(sizePolicy2)
        self.downloadTools_btn.setFont(font)
        icon2 = QIcon(QIcon.fromTheme(u"go-down"))
        self.downloadTools_btn.setIcon(icon2)

        self.gridLayout.addWidget(self.downloadTools_btn, 0, 0, 1, 1)

        self.pack_btn = QPushButton(self.centralwidget)
        self.pack_btn.setObjectName(u"pack_btn")
        self.pack_btn.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.pack_btn.sizePolicy().hasHeightForWidth())
        self.pack_btn.setSizePolicy(sizePolicy2)
        self.pack_btn.setFont(font)
        icon3 = QIcon(QIcon.fromTheme(u"document-save"))
        self.pack_btn.setIcon(icon3)

        self.gridLayout.addWidget(self.pack_btn, 1, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.status_lbl = QLabel(self.centralwidget)
        self.status_lbl.setObjectName(u"status_lbl")

        self.horizontalLayout_2.addWidget(self.status_lbl)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.exit_btn = QPushButton(self.centralwidget)
        self.exit_btn.setObjectName(u"exit_btn")
        icon4 = QIcon(QIcon.fromTheme(u"window-close"))
        self.exit_btn.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.exit_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 680, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Wii Menu Patcher", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Wii Menu Patcher", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"By NinjaCheetah", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Selected WAD:", None))
        self.selectWAD_btn.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.cleanUp_btn.setText(QCoreApplication.translate("MainWindow", u"Clean Up", None))
        self.extract_btn.setText(QCoreApplication.translate("MainWindow", u"Extract", None))
        self.downloadTools_btn.setText(QCoreApplication.translate("MainWindow", u"Download Tools", None))
        self.pack_btn.setText(QCoreApplication.translate("MainWindow", u"Pack", None))
        self.status_lbl.setText(QCoreApplication.translate("MainWindow", u"Ready. (No Tools)", None))
        self.exit_btn.setText(QCoreApplication.translate("MainWindow", u"Close", None))
    # retranslateUi

