from PySide6.QtWidgets import QMainWindow
from base1_ui import Ui_MainWindow

from PySide6.QtWidgets import (
QApplication,
QWidget,
QPushButton,
QMessageBox,
QFileDialog,
QVBoxLayout
)


class UiBridge(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #self.conectar_eventos()

        def conectar_eventos(self):
            ruta = self.ui.btnAddFilesToSave.clicked.connect(self.seleccionar_ruta)
            print(ruta)
            #self.ui.btnAddFilesToSave.clicked.connect(self.btn_addFilesAndFolders)

            def seleccionar_ruta(self):
                opciones = QFileDialog.Option.DontUseNativeDialog
                dialogo = QFileDialog(self)
                dialogo.setWindowTitle("Selecciona un archivo o carpeta")
                dialogo.setFileMode(QFileDialog.FileMode.ExistingFiles)
                dialogo.setOptions(opciones)

                if dialogo.exec():
                    rutas = dialogo.selectedFiles()
                    if rutas:
                        return rutas[0]
                    return None


                def btn_addFilesAndFolders(self):

                    self.showAlert("Botón presionado")

                    def showAlert(self, cad):
                        QMessageBox.information(
                        self,
                        "My first alert mf",
                        cad
                        )
