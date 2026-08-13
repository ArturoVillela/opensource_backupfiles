from PySide6.QtWidgets import QMainWindow
from base8_ui import Ui_MainWindow
from pathlib import Path
from PySide6 import QtCore

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

#btnSelectToFolder

class UiBridge(QMainWindow):

    def __init__(self):
        super().__init__()

        self.listPathsDir: list[str] = []
        self.listAllFilesToCopy: list[tuple[str, float]] = []
        self.finalPath: str = ""

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.vl_AddFilesToPath.setAlignment(
            Qt.AlignmentFlag.AlignTop
        )

        self.ui.vl_AddFilesToPath.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)


        self.ui.vl_AddFilesToPath.setSpacing(4)
        self.ui.vl_AddFilesToPath.setContentsMargins(5, 5, 5, 5)

        self.conectar_eventos()


    def conectar_eventos(self):
        self.ui.btnAddFilesToSave.clicked.connect(self.btnAddFilesToBackupClicked)
        self.ui.btnAddFolders.clicked.connect(self.btnAddFoldersToBackupClicked)
        self.ui.btnSelectToFolder.clicked.connect(self.btnSelectEndFolderClicked)
        self.ui.btn_clear_all.clicked.connect(self.btnClearAllClicked)


    def btnClearAllClicked(self):
        self.listAllFilesToCopy.clear()
        self.updateLabelInfoFiles("")
        print("aki limpiamos el layout de archivos")


    def btnAddFilesToBackupClicked(self):
        ruta, size = self.seleccionar_ruta()
        self.listAllFilesToCopy.append((ruta, size))
        ruta2 = Utils.formatear_ruta(ruta)
        formated_size = Utils.format_size(size)
        self.addPathIntoScrollPath(ruta2, formated_size)


    def btnAddFoldersToBackupClicked(self):
        ruta = self.seleccionarFolder()
        listTemp, fullSize = Utils.get_all_files_in_folder(ruta)   #returns a list of all files
        self.listAllFilesToCopy.extend(listTemp)                   #agrega todos los archivos a la lista
        sizeFormated = Utils.format_size(fullSize)
        ruta2 = Utils.formatear_ruta(ruta)
        print("la ruta seleccionada es: "+ruta)
        self.addPathIntoScrollPath(ruta, sizeFormated)


    def updateLabelInfoFiles(self, info):
        self.ui.label_all_files_to_copy.setText(info)


    def btnSelectEndFolderClicked(self):
        ruta = self.seleccionarFolder()
        self.finalPath = ruta
        ruta = Utils.formatear_ruta(ruta)
        self.ui.etToFolder.setText(ruta)


    def seleccionar_ruta(self):
        opciones = QFileDialog.Option.DontUseNativeDialog
        dialogo = QFileDialog(self)
        dialogo.setWindowTitle("Selecciona un archivo")
        dialogo.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialogo.setOptions(opciones)

        if dialogo.exec():
            rutas = dialogo.selectedFiles()
            if rutas:
                return rutas[0], Path(str(rutas[0])).stat().st_size
            return None, None


    def seleccionarFolder(self):
        opciones = QFileDialog.Option.DontUseNativeDialog
        dialogo = QFileDialog(self)
        dialogo.setOptions(opciones)

        dialogo.setWindowTitle("Selecciona una carpeta")
        dialogo.setFileMode(QFileDialog.FileMode.Directory)

        if dialogo.exec():
            rutas = dialogo.selectedFiles()

            if rutas:
                return rutas[0]

        return None


#    def addPathIntoScrollPath(self, path, size):
#        labelRuta = QLabel(Utils.formatStringWithSize(path, size))
#        labelRuta.setWordWrap(True)
#        self.ui.vl_AddFilesToPath.addWidget(labelRuta)
        #vl_AddFilesToPath


    def addPathIntoScrollPath(self, path, size):
        row = QWidget()
        row.setFixedHeight(30)
        row.setStyleSheet("border: none;")

        row_layout = QHBoxLayout(row)
        row_layout.setContentsMargins(0, 0, 0, 0)
        row_layout.setSpacing(10)

        label_ruta = QLabel(path)
        label_ruta.setFixedWidth(1000)
        label_ruta.setStyleSheet("border: none;")
        label_ruta.setAlignment(
                QtCore.Qt.AlignmentFlag.AlignLeft
                | QtCore.Qt.AlignmentFlag.AlignVCenter
            )

        label_size = QLabel(size)
        label_size.setFixedWidth(200)
        label_size.setStyleSheet("border: none;")

        row_layout.addWidget(label_ruta)
        row_layout.addWidget(label_size)

        self.ui.vl_AddFilesToPath.addWidget(row)


#    def btn_addFilesAndFolders(self):

#        self.showAlert("Botón presionado")

#        def showAlert(self, cad):
#            QMessageBox.information(
#            self,
#            "My first alert mf",
#            cad
#            )
