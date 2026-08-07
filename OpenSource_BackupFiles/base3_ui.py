# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'base1.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1080, 720)
        MainWindow.setMinimumSize(QSize(1080, 720))
        MainWindow.setMaximumSize(QSize(1080, 720))
        MainWindow.setMouseTracking(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.scrollToSave = QScrollArea(self.centralwidget)
        self.scrollToSave.setObjectName(u"scrollToSave")
        self.scrollToSave.setGeometry(QRect(30, 110, 291, 421))
        self.scrollToSave.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 287, 417))
        self.verticalLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 271, 391))
        self.vl_AddFilesToPath = QVBoxLayout(self.verticalLayoutWidget)
        self.vl_AddFilesToPath.setObjectName(u"vl_AddFilesToPath")
        self.vl_AddFilesToPath.setContentsMargins(0, 0, 0, 0)
        self.scrollToSave.setWidget(self.scrollAreaWidgetContents)
        self.btnAddFilesToSave = QPushButton(self.centralwidget)
        self.btnAddFilesToSave.setObjectName(u"btnAddFilesToSave")
        self.btnAddFilesToSave.setGeometry(QRect(30, 30, 291, 28))
        self.btnSelectToFolder = QPushButton(self.centralwidget)
        self.btnSelectToFolder.setObjectName(u"btnSelectToFolder")
        self.btnSelectToFolder.setGeometry(QRect(30, 550, 291, 28))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(False)
        self.frame.setGeometry(QRect(380, 30, 661, 591))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 181, 20))
        self.scrollAreaSaved = QScrollArea(self.frame)
        self.scrollAreaSaved.setObjectName(u"scrollAreaSaved")
        self.scrollAreaSaved.setGeometry(QRect(20, 90, 281, 451))
        self.scrollAreaSaved.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 277, 447))
        self.scrollAreaSaved.setWidget(self.scrollAreaWidgetContents_2)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 60, 261, 20))
        self.scrollAreaConflicts = QScrollArea(self.frame)
        self.scrollAreaConflicts.setObjectName(u"scrollAreaConflicts")
        self.scrollAreaConflicts.setGeometry(QRect(340, 90, 281, 451))
        self.scrollAreaConflicts.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 277, 447))
        self.scrollAreaConflicts.setWidget(self.scrollAreaWidgetContents_3)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(340, 60, 261, 20))
        self.etToFolder = QLineEdit(self.centralwidget)
        self.etToFolder.setObjectName(u"etToFolder")
        self.etToFolder.setEnabled(False)
        self.etToFolder.setGeometry(QRect(30, 590, 291, 28))
        self.etToFolder.setReadOnly(True)
        self.btnStartStop = QPushButton(self.centralwidget)
        self.btnStartStop.setObjectName(u"btnStartStop")
        self.btnStartStop.setEnabled(False)
        self.btnStartStop.setGeometry(QRect(30, 640, 1011, 28))
        self.btnStartStop.setCheckable(False)
        self.btnAddFolders = QPushButton(self.centralwidget)
        self.btnAddFolders.setObjectName(u"btnAddFolders")
        self.btnAddFolders.setGeometry(QRect(30, 70, 291, 28))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1080, 30))
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuhelp = QMenu(self.menubar)
        self.menuhelp.setObjectName(u"menuhelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnAddFilesToSave.setText(QCoreApplication.translate("MainWindow", u"Add files to Save", None))
        self.btnSelectToFolder.setText(QCoreApplication.translate("MainWindow", u"Select To Folder", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Progress and Conflics", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Saved files", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Conflicts", None))
        self.etToFolder.setText(QCoreApplication.translate("MainWindow", u"/Home/..", None))
        self.btnStartStop.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btnAddFolders.setText(QCoreApplication.translate("MainWindow", u"Add Folders to Save", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuhelp.setTitle(QCoreApplication.translate("MainWindow", u"help", None))
    # retranslateUi

