from PySide6.QtWidgets import QMainWindow
from base3_ui import Ui_MainWindow

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


class UiBridge(QMainWindow):

    def __init__(self):
        super().__init__()

        self.listPathsFiles: list[str] = []
        self.listPathsDir: list[str] = []
        self.finalPath: str = ""

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.layoutRutas = QVBoxLayout(self.ui.scrollAreaWidgetContents)
        self.layoutRutas.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.ui.vl_AddFilesToPath.setAlignment(
            Qt.AlignmentFlag.AlignTop
        )

        self.ui.vl_AddFilesToPath.setSpacing(4)
        self.ui.vl_AddFilesToPath.setContentsMargins(5, 5, 5, 5)

        self.conectar_eventos()


    def conectar_eventos(self):
        self.ui.btnAddFilesToSave.clicked.connect(self.btnAddFilesToBackupClicked)
        self.ui.btnAddFolders.clicked.connect(self.btnAddFoldersToBackupClicked)
        self.ui.btnSelectToFolder.clicked.connect(self.btnSelectEndFolderClicked)



    def btnAddFilesToBackupClicked(self):
        ruta = self.seleccionar_ruta()
        self.listPathsFiles.append(ruta)
        ruta = Utils.formatear_ruta(ruta)
        print("la ruta seleccionada es: "+ruta)
        self.addPathIntoScrollPath(ruta)


    def btnAddFoldersToBackupClicked(self):
        ruta = self.seleccionarFolder()
        print(ruta)
        self.listPathsFiles.append(ruta)
        ruta = Utils.formatear_ruta(ruta)
        print("la ruta seleccionada es: "+ruta)
        self.addPathIntoScrollPath(ruta)


    def btnSelectEndFolderClicked(self):
        ruta = self.seleccionar_ruta()
        self.finalPath = ruta
        ruta = Utils.formatear_ruta(ruta)
        self.ui.etToFolder.setText(ruta)



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
