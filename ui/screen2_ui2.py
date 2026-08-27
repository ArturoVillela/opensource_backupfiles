# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'second_screen.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1067, 824)
        Form.setStyleSheet(u"background-color: rgb(224, 255, 252);")
        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 490, 1051, 211))
        self.frame_3.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid #7f7e7d;\n"
"}\n"
"\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.widget_4 = QWidget(self.frame_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(10, 100, 1021, 101))
        self.widget_4.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"    border: 2px solid #E5E5E5;\n"
"}")
        self.pushButton = QPushButton(self.widget_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(800, 40, 81, 41))
        self.pushButton.setStyleSheet(u"QPushButton#toggleButton {\n"
"    border: none;\n"
"    border-image: url(\"/home/charlito/Documents/dev/python/figma/toggleBtnOff.png\");\n"
"}\n"
"\n"
"QPushButton#toggleButton:checked {\n"
"    border-image: url(\"/home/charlito/Documents/dev/python/figma/toggleBtnOn.png\");\n"
"}")
        icon = QIcon()
        icon.addFile(u"../../figma/toogleBtnOff.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(80, 40))
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(True)
        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 151, 21))
        self.label_4 = QLabel(self.widget_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 40, 631, 31))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_5 = QLabel(self.widget_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(710, 50, 76, 20))
        self.label_6 = QLabel(self.widget_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(900, 50, 91, 20))
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 41, 31))
        self.label.setPixmap(QPixmap(u"../../figma/ic_alert.png"))
        self.label.setScaledContents(True)
        self.label_conflic = QLabel(self.frame_3)
        self.label_conflic.setObjectName(u"label_conflic")
        self.label_conflic.setGeometry(QRect(50, 20, 341, 31))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.label_conflic.setFont(font1)
        self.label_conflic.setStyleSheet(u"color: rgb(220, 3, 6);")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 70, 921, 20))
        self.containerLwidget_s2 = QWidget(Form)
        self.containerLwidget_s2.setObjectName(u"containerLwidget_s2")
        self.containerLwidget_s2.setGeometry(QRect(10, 30, 1041, 431))
        self.containerLwidget_s2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_7 = QLabel(self.containerLwidget_s2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 20, 41, 31))
        self.label_7.setPixmap(QPixmap(u"../../figma/ic_alert.png"))
        self.label_7.setScaledContents(True)
        self.label_conflic_2 = QLabel(self.containerLwidget_s2)
        self.label_conflic_2.setObjectName(u"label_conflic_2")
        self.label_conflic_2.setGeometry(QRect(70, 20, 341, 41))
        self.label_conflic_2.setFont(font1)
        self.label_conflic_2.setStyleSheet(u"color: rgb(220, 3, 6);")
        self.label_8 = QLabel(self.containerLwidget_s2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 60, 591, 20))
        self.scrollArea = QScrollArea(self.containerLwidget_s2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(20, 100, 1001, 271))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 997, 267))
        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 991, 261))
        self.verticalLayoutWidget_2 = QWidget(self.widget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 10, 971, 355))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_conflic_3 = QLabel(self.verticalLayoutWidget_2)
        self.label_conflic_3.setObjectName(u"label_conflic_3")
        self.label_conflic_3.setFont(font1)
        self.label_conflic_3.setStyleSheet(u"color: rgb(220, 3, 6);")

        self.verticalLayout_2.addWidget(self.label_conflic_3)

        self.label_conflic_6 = QLabel(self.verticalLayoutWidget_2)
        self.label_conflic_6.setObjectName(u"label_conflic_6")
        self.label_conflic_6.setFont(font1)
        self.label_conflic_6.setStyleSheet(u"color: rgb(220, 3, 6);")

        self.verticalLayout_2.addWidget(self.label_conflic_6)

        self.label_conflic_7 = QLabel(self.verticalLayoutWidget_2)
        self.label_conflic_7.setObjectName(u"label_conflic_7")
        self.label_conflic_7.setFont(font1)
        self.label_conflic_7.setStyleSheet(u"color: rgb(220, 3, 6);")

        self.verticalLayout_2.addWidget(self.label_conflic_7)

        self.label_conflic_9 = QLabel(self.verticalLayoutWidget_2)
        self.label_conflic_9.setObjectName(u"label_conflic_9")
        self.label_conflic_9.setFont(font1)
        self.label_conflic_9.setStyleSheet(u"color: rgb(220, 3, 6);")

        self.verticalLayout_2.addWidget(self.label_conflic_9)

        self.label_conflic_8 = QLabel(self.verticalLayoutWidget_2)
        self.label_conflic_8.setObjectName(u"label_conflic_8")
        self.label_conflic_8.setFont(font1)
        self.label_conflic_8.setStyleSheet(u"color: rgb(220, 3, 6);")

        self.verticalLayout_2.addWidget(self.label_conflic_8)

        self.label_conflic_10 = QLabel(self.verticalLayoutWidget_2)
        self.label_conflic_10.setObjectName(u"label_conflic_10")
        self.label_conflic_10.setFont(font1)
        self.label_conflic_10.setStyleSheet(u"color: rgb(220, 3, 6);")

        self.verticalLayout_2.addWidget(self.label_conflic_10)

        self.label_conflic_5 = QLabel(self.verticalLayoutWidget_2)
        self.label_conflic_5.setObjectName(u"label_conflic_5")
        self.label_conflic_5.setFont(font1)
        self.label_conflic_5.setStyleSheet(u"color: rgb(220, 3, 6);")

        self.verticalLayout_2.addWidget(self.label_conflic_5)

        self.label_conflic_4 = QLabel(self.verticalLayoutWidget_2)
        self.label_conflic_4.setObjectName(u"label_conflic_4")
        self.label_conflic_4.setFont(font1)
        self.label_conflic_4.setStyleSheet(u"color: rgb(220, 3, 6);")

        self.verticalLayout_2.addWidget(self.label_conflic_4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"Filename:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"/Home/Documents/..../myFile.jav   Destination (2.3gb ) origen (1.1gb)", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Ignore", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Overwrite", None))
        self.label.setText("")
        self.label_conflic.setText(QCoreApplication.translate("Form", u"Conflict Detected", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Please review all files conflicts, this files already exists in the  destination", None))
        self.label_7.setText("")
        self.label_conflic_2.setText(QCoreApplication.translate("Form", u"Conflict Detected", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Please review all files conflicts, this files already exists in the  destination", None))
        self.label_conflic_3.setText(QCoreApplication.translate("Form", u"Conflict Detected", None))
        self.label_conflic_6.setText(QCoreApplication.translate("Form", u"Conflict Detected", None))
        self.label_conflic_7.setText(QCoreApplication.translate("Form", u"Conflict Detected", None))
        self.label_conflic_9.setText(QCoreApplication.translate("Form", u"Conflict Detected", None))
        self.label_conflic_8.setText(QCoreApplication.translate("Form", u"Conflict Detected", None))
        self.label_conflic_10.setText(QCoreApplication.translate("Form", u"Conflict Detected", None))
        self.label_conflic_5.setText(QCoreApplication.translate("Form", u"Conflict Detected", None))
        self.label_conflic_4.setText(QCoreApplication.translate("Form", u"Conflict Detected", None))
    # retranslateUi

