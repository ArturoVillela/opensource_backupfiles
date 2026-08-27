from PySide6.QtWidgets import QMainWindow
#from base8_ui import Ui_MainWindow
from screen2_ui2 import Ui_Form
from pathlib import Path
from PySide6 import QtCore
from Resources import Resources
from PySide6.QtCore import QObject, QThread, Signal, Qt
from PySide6.QtWidgets import QProgressDialog

from PySide6.QtWidgets import (
QApplication,
QWidget,
QPushButton,
QMessageBox,
QFileDialog,
QVBoxLayout,
QLabel
)
from PySide6.QtCore import Qt
from Utils import Utils
from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout
from CopyFiles import CopyFiles


class UiBridge2(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

#        self.ui.vl_AddFilesToPath.setAlignment(
#            Qt.AlignmentFlag.AlignTop
#        )

#        self.ui.vl_AddFilesToPath.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
#        self.ui.vl_AddFilesToPath.setSpacing(4)
#        self.ui.vl_AddFilesToPath.setContentsMargins(5, 5, 5, 5)

