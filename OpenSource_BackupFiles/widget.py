# This Python file uses the following encoding: utf-8
# comando para exportar el ui a python pyside6-uic base1.ui -o base3_ui.py
# Shift + Tab: mueve todo el bloque 4 espacios hacia la izquierda.
# Tab: mueve todo el bloque 4 espacios hacia la derecha.

import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QMessageBox,
    QVBoxLayout
)
# from ui_bridge2 import UiBridge2    este es para ejecutar la segunda pantalla al inicio
# vl_AddFilesToPath es el layout donde ponemos los labels
from ui_bridge import UiBridge


class Widget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Mi primera app")

        # Layout
        layout = QVBoxLayout()

        self.button = QPushButton("click me mf")
        self.button.clicked.connect(self.showAlert)

        layout.addWidget(self.button)
        self.setLayout(layout)


    def showAlert(self):
        QMessageBox.information(
                     self,
                     "My first alert mf",
                     "halo moto... "
                 )


if __name__ == "__main__":
    app = QApplication(sys.argv)

#    window = UiBridge2()    #esta se usa para inicializar la segunda pantalla...
    window = UiBridge()
    window.show()

    sys.exit(app.exec())




#if __name__ == "__main__":
#    app = QApplication([])
#    window = Widget()
#    window.show()
#    sys.exit(app.exec_())
