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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(799, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setTextFormat(Qt.AutoText)

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabsClosable(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_4 = QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_3 = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(15)
        self.label_3.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_3)

        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)

        self.verticalSpacer_2 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")
        font2 = QFont()
        font2.setPointSize(12)
        self.label_6.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_6)

        self.selectWAD_btn = QPushButton(self.tab)
        self.selectWAD_btn.setObjectName(u"selectWAD_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectWAD_btn.sizePolicy().hasHeightForWidth())
        self.selectWAD_btn.setSizePolicy(sizePolicy)
        self.selectWAD_btn.setMinimumSize(QSize(0, 50))

        self.verticalLayout_5.addWidget(self.selectWAD_btn)

        self.WADstatus_lbl = QLabel(self.tab)
        self.WADstatus_lbl.setObjectName(u"WADstatus_lbl")
        self.WADstatus_lbl.setMinimumSize(QSize(0, 60))
        self.WADstatus_lbl.setTextFormat(Qt.MarkdownText)
        self.WADstatus_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_5.addWidget(self.WADstatus_lbl)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.verticalLayout_6.addWidget(self.label_5)

        self.downloadTools_btn = QPushButton(self.tab)
        self.downloadTools_btn.setObjectName(u"downloadTools_btn")
        self.downloadTools_btn.setMinimumSize(QSize(0, 50))

        self.verticalLayout_6.addWidget(self.downloadTools_btn)

        self.toolStatus_lbl = QLabel(self.tab)
        self.toolStatus_lbl.setObjectName(u"toolStatus_lbl")
        self.toolStatus_lbl.setMinimumSize(QSize(0, 60))
        self.toolStatus_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_6.addWidget(self.toolStatus_lbl)


        self.horizontalLayout.addLayout(self.verticalLayout_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.status_lbl = QLabel(self.centralwidget)
        self.status_lbl.setObjectName(u"status_lbl")

        self.horizontalLayout_2.addWidget(self.status_lbl)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy1)
        self.progressBar.setMinimumSize(QSize(250, 0))
        self.progressBar.setMaximumSize(QSize(16777215, 16777208))
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.progressBar.setTextVisible(True)

        self.horizontalLayout_2.addWidget(self.progressBar)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 799, 30))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Wii Menu Patcher", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"v0.1", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Welcome to the Wii Menu Patcher!", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"To begin, select the WAD you wish to modify, and download the required external tools.", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"System Menu WAD", None))
        self.selectWAD_btn.setText(QCoreApplication.translate("MainWindow", u"Choose WAD", None))
        self.WADstatus_lbl.setText(QCoreApplication.translate("MainWindow", u"None currently selected.", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.downloadTools_btn.setText(QCoreApplication.translate("MainWindow", u"Download Tools", None))
        self.toolStatus_lbl.setText(QCoreApplication.translate("MainWindow", u"Tools currently not downloaded.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Home", None))
        self.status_lbl.setText(QCoreApplication.translate("MainWindow", u"Ready. (Tools Not Present)", None))
    # retranslateUi

