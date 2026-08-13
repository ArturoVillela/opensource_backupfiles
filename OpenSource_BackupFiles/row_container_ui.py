# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'file_row.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1118, 132)
        self.qframe_container_row = QFrame(Form)
        self.qframe_container_row.setObjectName(u"qframe_container_row")
        self.qframe_container_row.setGeometry(QRect(10, 20, 1071, 61))
        self.qframe_container_row.setStyleSheet(u"background-color: rgb(244, 244, 244);")
        self.qframe_container_row.setFrameShape(QFrame.StyledPanel)
        self.qframe_container_row.setFrameShadow(QFrame.Raised)
        self.horizontalLayoutWidget = QWidget(self.qframe_container_row)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 1051, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_path = QLabel(self.horizontalLayoutWidget)
        self.lb_path.setObjectName(u"lb_path")
        self.lb_path.setEnabled(True)

        self.horizontalLayout.addWidget(self.lb_path)

        self.label_size = QLabel(self.horizontalLayoutWidget)
        self.label_size.setObjectName(u"label_size")
        self.label_size.setEnabled(True)

        self.horizontalLayout.addWidget(self.label_size)

        self.btn_delete = QPushButton(self.horizontalLayoutWidget)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"../../figma/ic_trash.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_delete.setIcon(icon)

        self.horizontalLayout.addWidget(self.btn_delete)

        self.horizontalLayout.setStretch(0, 10)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lb_path.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_size.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.btn_delete.setText("")
    # retranslateUi

