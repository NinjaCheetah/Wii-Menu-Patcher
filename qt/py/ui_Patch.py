# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Patch.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QListView,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Patch(object):
    def setupUi(self, Patch):
        if not Patch.objectName():
            Patch.setObjectName(u"Patch")
        Patch.resize(777, 398)
        self.verticalLayout_2 = QVBoxLayout(Patch)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Patch)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(Patch)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_2)

        self.wadInfo_lbl = QLabel(Patch)
        self.wadInfo_lbl.setObjectName(u"wadInfo_lbl")
        self.wadInfo_lbl.setMinimumSize(QSize(0, 60))
        self.wadInfo_lbl.setTextFormat(Qt.MarkdownText)

        self.verticalLayout_3.addWidget(self.wadInfo_lbl)

        self.label_3 = QLabel(Patch)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QSize(16777215, 16777215))
        self.label_3.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_3)

        self.verticalSpacer = QSpacerItem(20, 175, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.listView = QListView(Patch)
        self.listView.setObjectName(u"listView")

        self.horizontalLayout.addWidget(self.listView)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Patch)

        QMetaObject.connectSlotsByName(Patch)
    # setupUi

    def retranslateUi(self, Patch):
        Patch.setWindowTitle(QCoreApplication.translate("Patch", u"Form", None))
        self.label.setText(QCoreApplication.translate("Patch", u"Patch", None))
        self.label_2.setText(QCoreApplication.translate("Patch", u"Your System Menu:", None))
        self.wadInfo_lbl.setText("")
        self.label_3.setText(QCoreApplication.translate("Patch", u"To begin, select a patch from the tree on the right that you'd like to apply.", None))
    # retranslateUi

