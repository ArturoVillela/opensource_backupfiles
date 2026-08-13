# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6 import QtWidgets
from row_container_ui3 import Ui_Form



#class FileRow(QtWidgets.QWidget):
#    def __init__(self):
#        pass

class FileRow(QtWidgets.QWidget):

    def __init__(self, path, size, position, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.lb_path.setText(path)
        self.ui.label_size.setText(size)

        if position % 2 == 0:
            background_color = "white"
        else:
            background_color = "#F2F2F2"

        self.ui.qframe_container_row.setStyleSheet(
            f"background-color: {background_color};"
        )

        self.setFixedHeight(60)
        self.setFixedWidth(1050)
