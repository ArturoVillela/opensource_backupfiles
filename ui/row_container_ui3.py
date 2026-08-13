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
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1118, 132)
        self.qframe_container_row = QFrame(Form)
        self.qframe_container_row.setObjectName(u"qframe_container_row")
        self.qframe_container_row.setGeometry(QRect(10, 20, 1061, 48))
        self.qframe_container_row.setStyleSheet(u"background-color: rgb(244, 244, 244);")
        self.qframe_container_row.setFrameShape(QFrame.StyledPanel)
        self.qframe_container_row.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.qframe_container_row)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_path = QLabel(self.qframe_container_row)
        self.lb_path.setObjectName(u"lb_path")
        self.lb_path.setEnabled(True)

        self.horizontalLayout.addWidget(self.lb_path)

        self.label_size = QLabel(self.qframe_container_row)
        self.label_size.setObjectName(u"label_size")
        self.label_size.setEnabled(True)

        self.horizontalLayout.addWidget(self.label_size)

        self.horizontalLayout.setStretch(0, 10)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lb_path.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_size.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

