from PySide6.QtWidgets import QMainWindow
from base6_ui import Ui_MainWindow
from pathlib import Path
from FileRow import FileRow
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

#btnSelectToFolder

class UiBridge(QMainWindow):

    def __init__(self):
        super().__init__()

        self.listPathsDir: list[str] = []
        self.listAllFilesToCopy: list[tuple[str, float]] = []
        self.finalPath: str = ""

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.layoutRutas = QVBoxLayout(self.ui.scrollAreaWidgetContents_4)
        self.layoutRutas.setAlignment(Qt.AlignmentFlag.AlignTop)

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
        self.ui.pushButton.clicked.connect(self.btnClearAllClicked)
        #pushButton  -> cambiado a btn_clear_all


    def btnClearAllClicked(self):
        self.listAllFilesToCopy.clear()


    def btnAddFilesToBackupClicked(self):
        ruta = self.seleccionar_ruta()
        ruta, size = Utils.formatear_ruta(ruta)
        self.listAllFilesToCopy.append((ruta, size))
        formated_size = Utils.format_size(size)
        print("la ruta seleccionada es: "+ruta+" size :"+ formated_size)
        row_details = FileRow (ruta, str(size), len(self.listAllFilesToCopy))
        self.ui.vl_AddFilesToPath.addWidget(row_details)
        print("Elementos en el layout:", self.ui.vl_AddFilesToPath.count())
        row_details.show()
#        self.addPathIntoScrollPath(ruta)


    def btnAddFoldersToBackupClicked(self):
        ruta = self.seleccionarFolder()
        listTemp = Utils.get_all_files_in_folder(ruta)
        self.listAllFilesToCopy.extend(listTemp)
        ruta = Utils.formatear_ruta(ruta)
        print("la ruta seleccionada es: "+ruta)
        self.addPathIntoScrollPath(ruta)


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
            return None


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


    def addPathIntoScrollPath(self, path):
        labelRuta = QLabel(path)
        labelRuta.setWordWrap(True)
        self.ui.vl_AddFilesToPath.addWidget(labelRuta)



#    def btn_addFilesAndFolders(self):

#        self.showAlert("Botón presionado")

#        def showAlert(self, cad):
#            QMessageBox.information(
#            self,
#            "My first alert mf",
#            cad
#            )
