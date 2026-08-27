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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QStackedWidget,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1080, 700)
        MainWindow.setMinimumSize(QSize(1080, 700))
        MainWindow.setMaximumSize(QSize(1999, 700))
        MainWindow.setMouseTracking(True)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 1111, 671))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(231, 243, 255);")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.frame_2 = QFrame(self.page_1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 10, 1061, 411))
        self.frame_2.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid #7f7e7d;\n"
"}\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 10, 201, 20))
        font = QFont()
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"QLabel {\n"
"    border: none;\n"
"}")
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 10, 21, 20))
        self.label_6.setStyleSheet(u"QLabel {\n"
"    border: none;\n"
"}")
        self.label_6.setPixmap(QPixmap(u"../../figma/ic_folder.png"))
        self.btnAddFilesToSave = QPushButton(self.frame_2)
        self.btnAddFilesToSave.setObjectName(u"btnAddFilesToSave")
        self.btnAddFilesToSave.setGeometry(QRect(790, 10, 121, 28))
        icon = QIcon()
        icon.addFile(u"../../figma/ic_add_file.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnAddFilesToSave.setIcon(icon)
        self.btnAddFolders = QPushButton(self.frame_2)
        self.btnAddFolders.setObjectName(u"btnAddFolders")
        self.btnAddFolders.setGeometry(QRect(920, 10, 131, 28))
        icon1 = QIcon()
        icon1.addFile(u"../../figma/ic_add_folder.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnAddFolders.setIcon(icon1)
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 30, 401, 20))
        self.label_5.setStyleSheet(u"QLabel {\n"
"    border: none;\n"
"}")
        self.widget = QWidget(self.frame_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 60, 1041, 321))
        self.widget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"    border: 2px solid #E5E5E5;\n"
"}")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 0, 1041, 31))
        self.label_4.setStyleSheet(u"background-color: rgb(230, 239, 247);")
        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(9, 38, 1021, 271))
        self.scrollArea.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"    border: none;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1021, 271))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.btn_clear_all = QPushButton(self.frame_2)
        self.btn_clear_all.setObjectName(u"btn_clear_all")
        self.btn_clear_all.setGeometry(QRect(960, 380, 91, 28))
        self.btn_clear_all.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 255, 255);\n"
"    border: none;\n"
"    color: red;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"../../figma/ic_clear_all.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_clear_all.setIcon(icon2)
        self.label_all_files_to_copy = QLabel(self.frame_2)
        self.label_all_files_to_copy.setObjectName(u"label_all_files_to_copy")
        self.label_all_files_to_copy.setGeometry(QRect(20, 380, 411, 20))
        self.label_all_files_to_copy.setStyleSheet(u"QLabel {\n"
"    border: none;\n"
"}")
        self.frame_3 = QFrame(self.page_1)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 430, 1061, 141))
        self.frame_3.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid #7f7e7d;\n"
"}\n"
"\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_16 = QLabel(self.frame_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(40, 10, 201, 20))
        self.label_16.setFont(font)
        self.label_16.setStyleSheet(u"QLabel {\n"
"    border: none;\n"
"}")
        self.label_17 = QLabel(self.frame_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 10, 21, 20))
        self.label_17.setStyleSheet(u"QLabel {\n"
"    border: none;\n"
"}")
        self.label_17.setPixmap(QPixmap(u"../../figma/ic_backup.png"))
        self.label_18 = QLabel(self.frame_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 30, 401, 20))
        self.label_18.setStyleSheet(u"QLabel {\n"
"    border: none;\n"
"}")
        self.widget_4 = QWidget(self.frame_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(10, 70, 1041, 61))
        self.widget_4.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"    border: 2px solid #E5E5E5;\n"
"}")
        self.frame = QFrame(self.widget_4)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 851, 61))
        self.frame.setStyleSheet(u"background-color: rgb(230, 239, 247);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayoutWidget = QWidget(self.frame)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 831, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_img_disk = QLabel(self.horizontalLayoutWidget)
        self.label_img_disk.setObjectName(u"label_img_disk")
        self.label_img_disk.setEnabled(False)
        self.label_img_disk.setStyleSheet(u"QLabel {\n"
"    border: none;\n"
"}")
        self.label_img_disk.setPixmap(QPixmap(u"../../figma/ic_save.png"))

        self.horizontalLayout.addWidget(self.label_img_disk)

        self.etToFolder = QLineEdit(self.horizontalLayoutWidget)
        self.etToFolder.setObjectName(u"etToFolder")
        self.etToFolder.setEnabled(False)
        self.etToFolder.setReadOnly(True)

        self.horizontalLayout.addWidget(self.etToFolder)

        self.btnSelectToFolder = QPushButton(self.widget_4)
        self.btnSelectToFolder.setObjectName(u"btnSelectToFolder")
        self.btnSelectToFolder.setGeometry(QRect(880, 20, 131, 28))
        self.btnSelectToFolder.setIcon(icon1)
        self.btn_start = QPushButton(self.page_1)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setEnabled(True)
        self.btn_start.setGeometry(QRect(10, 590, 1061, 41))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.btn_start.setFont(font1)
        self.btn_start.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(62, 68, 154);\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(42, 47, 115);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"../../figma/ic_btn_start.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_start.setIcon(icon3)
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.containerLwidget_s2 = QWidget(self.page_2)
        self.containerLwidget_s2.setObjectName(u"containerLwidget_s2")
        self.containerLwidget_s2.setGeometry(QRect(10, 10, 1061, 561))
        self.containerLwidget_s2.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid #7f7e7d;\n"
"}\n"
"")
        self.label_8 = QLabel(self.containerLwidget_s2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 20, 41, 31))
        self.label_8.setStyleSheet(u"QLabel {\n"
"    border: none;\n"
"}\n"
"")
        self.label_8.setPixmap(QPixmap(u"../../figma/ic_alert.png"))
        self.label_8.setScaledContents(True)
        self.label_conflic_2 = QLabel(self.containerLwidget_s2)
        self.label_conflic_2.setObjectName(u"label_conflic_2")
        self.label_conflic_2.setGeometry(QRect(70, 20, 341, 41))
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.label_conflic_2.setFont(font2)
        self.label_conflic_2.setStyleSheet(u"QLabel {\n"
"color: rgb(220, 3, 6);\n"
"    border: none;\n"
"}\n"
"")
        self.labelXConflics = QLabel(self.containerLwidget_s2)
        self.labelXConflics.setObjectName(u"labelXConflics")
        self.labelXConflics.setGeometry(QRect(20, 60, 591, 31))
        font3 = QFont()
        font3.setPointSize(11)
        self.labelXConflics.setFont(font3)
        self.labelXConflics.setStyleSheet(u"QLabel {\n"
"    border: none;\n"
"}\n"
"")
        self.scrollArea_2 = QScrollArea(self.containerLwidget_s2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(20, 100, 1021, 381))
        self.scrollArea_2.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(235, 255, 253);\n"
"    border: 1px solid #e6e6e6;\n"
"}rgb(230, 230, 230)\n"
"")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1019, 379))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.btnCancelBackup = QPushButton(self.containerLwidget_s2)
        self.btnCancelBackup.setObjectName(u"btnCancelBackup")
        self.btnCancelBackup.setGeometry(QRect(870, 500, 171, 41))
        self.btnCancelBackup.setStyleSheet(u"QPushButton {\n"
"    background-color: #8a0000;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 6px 12px;\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"../../figma/ic_cancel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnCancelBackup.setIcon(icon4)
        self.btnSkipAll = QPushButton(self.containerLwidget_s2)
        self.btnSkipAll.setObjectName(u"btnSkipAll")
        self.btnSkipAll.setGeometry(QRect(740, 50, 121, 41))
        font4 = QFont()
        font4.setPointSize(10)
        self.btnSkipAll.setFont(font4)
        self.btnSkipAll.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFFFFF;\n"
"    color: black;\n"
"    border-radius: 5px;\n"
"    padding: 6px 12px;\n"
"}\n"
"")
        self.btnSkipAll.setIcon(icon4)
        self.btnOverwritteAll = QPushButton(self.containerLwidget_s2)
        self.btnOverwritteAll.setObjectName(u"btnOverwritteAll")
        self.btnOverwritteAll.setGeometry(QRect(870, 50, 171, 41))
        self.btnOverwritteAll.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFFFFF;\n"
"    color: black;\n"
"    border-radius: 5px;\n"
"    padding: 6px 12px;\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"../../figma/ic_ok2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnOverwritteAll.setIcon(icon5)
        self.btnStartBackup2 = QPushButton(self.page_2)
        self.btnStartBackup2.setObjectName(u"btnStartBackup2")
        self.btnStartBackup2.setEnabled(True)
        self.btnStartBackup2.setGeometry(QRect(10, 590, 1061, 41))
        self.btnStartBackup2.setFont(font1)
        self.btnStartBackup2.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(62, 68, 154);\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(42, 47, 115);\n"
"}")
        self.btnStartBackup2.setIcon(icon3)
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1080, 30))
        self.menubar.setStyleSheet(u"background-color: rgb(243, 243, 243);s")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuAbout.setLayoutDirection(Qt.RightToLeft)
        self.menuhelp = QMenu(self.menubar)
        self.menuhelp.setObjectName(u"menuhelp")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Source Files & Folders", None))
        self.label_6.setText("")
        self.btnAddFilesToSave.setText(QCoreApplication.translate("MainWindow", u"Add File", None))
        self.btnAddFolders.setText(QCoreApplication.translate("MainWindow", u"Add Folder", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Select Files and Folders to back up", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"  Path                                                                                                                                                                                                                                                     size", None))
        self.btn_clear_all.setText(QCoreApplication.translate("MainWindow", u" Clear All", None))
        self.label_all_files_to_copy.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Backup Destination", None))
        self.label_17.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Select target drive or folder", None))
        self.label_img_disk.setText("")
        self.etToFolder.setText(QCoreApplication.translate("MainWindow", u"/Home/..", None))
        self.btnSelectToFolder.setText(QCoreApplication.translate("MainWindow", u"Add Folder", None))
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u" Start", None))
        self.label_8.setText("")
        self.label_conflic_2.setText(QCoreApplication.translate("MainWindow", u"Conflicts Detected", None))
        self.labelXConflics.setText(QCoreApplication.translate("MainWindow", u"XX files conflicts detected, click file for details.", None))
        self.btnCancelBackup.setText(QCoreApplication.translate("MainWindow", u" Cancel Backup", None))
        self.btnSkipAll.setText(QCoreApplication.translate("MainWindow", u"Skip All", None))
        self.btnOverwritteAll.setText(QCoreApplication.translate("MainWindow", u" Overwritte All", None))
        self.btnStartBackup2.setText(QCoreApplication.translate("MainWindow", u" Start Backup", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.menuhelp.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

