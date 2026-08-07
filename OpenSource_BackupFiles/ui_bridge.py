from PySide6.QtWidgets import QMainWindow
from base2_ui import Ui_MainWindow

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

        self.listPaths: list[str] = []

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
        self.ui.btnAddFilesToSave.clicked.connect(self.btnAddFolderClicked)
        self.ui.btnSelectToFolder.clicked.connect(self.btnSelectEndFolderClicked)


    def btnAddFolderClicked(self):
        ruta = self.seleccionar_ruta()
        self.listPaths.append(ruta)
        ruta = Utils.formatear_ruta(ruta)
        print("la ruta seleccionada es: "+ruta)
        self.addPathIntoScrollPath(ruta)


    def btnSelectEndFolderClicked(self):
        print("hola mundo....")
        ruta = self.seleccionar_ruta()



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
