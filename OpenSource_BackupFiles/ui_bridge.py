from PySide6.QtWidgets import QMainWindow
from base8_ui import Ui_MainWindow
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

#btnSelectToFolder

class UiBridge(QMainWindow):

    def __init__(self):
        super().__init__()

        self.listPathsDir: list[str] = []
        self.listAllFilesToCopy: list[tuple[str, float]] = []
        self.finalPath: str = ""
        self.copyFiles = CopyFiles()

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
        self.ui.btn_clear_all.clicked.connect(self.btnClearAllClicked)  #btn_start
        self.ui.btn_start.clicked.connect(self.btnStartClicked)


    def btnStartClicked(self):
#        if not self.listAllFilesToCopy:
#            title,subtitle = Resources().getDialogInfoByCode(2)
#            self.showAlert(title,subtitle)
#            return
#        if not self.finalPath:
#            title,subtitle = Resources().getDialogInfoByCode(1)
#            self.showAlert(title,subtitle)
#            return
        self.startingBuckup()
        print("btn start clicked!! a validar...")


    def btnClearAllClicked(self):
        self.listAllFilesToCopy.clear()
        self.updateLabelInfo()
        self.ui.label_all_files_to_copy.setText (" ")
        Utils.clearQBoxLayout(self.ui.vl_AddFilesToPath)
        print("aki limpiamos el layout de archivos, nuevo size : " +str(len(self.listAllFilesToCopy)))


    def btnAddFilesToBackupClicked(self):
        ruta, size = self.seleccionar_ruta()
        self.listAllFilesToCopy.append((ruta, size))
        ruta2 = Utils.formatear_ruta(ruta)
        formated_size = Utils.format_size(size)
        self.addPathIntoScrollPath(ruta2, formated_size)
        self.updateLabelInfo()

    def btnAddFoldersToBackupClicked(self):
        ruta = self.seleccionarFolder()
        listTemp, fullSize = Utils.get_all_files_in_folder(ruta)   #returns a list of all files
        listTupla = Utils.getTuplaListFromPathList(listTemp)
        self.listAllFilesToCopy.extend(listTupla)                   #error debe agrega la lista de tuplas
        sizeFormated = Utils.format_size(fullSize)
        ruta2 = Utils.formatear_ruta(ruta)
        print("la ruta seleccionada es: "+ruta)
        self.addPathIntoScrollPath(ruta, sizeFormated)
        self.updateLabelInfo()


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


    def updateLabelInfo(self):
        fullSize = Utils.getFinalListSize(self.listAllFilesToCopy)
        formatedSize = Utils.format_size(fullSize)
        print("pss se llamo con size :  "+formatedSize)
        self.ui.label_all_files_to_copy.setText ("All files to copy Size : " + str(formatedSize))


    def showAlert(self, title, subtitle):
        dialogo = QMessageBox(self)
        dialogo.setWindowTitle(title)
        dialogo.setText(subtitle)
        dialogo.setIcon(Utils.getDialogIconByTitle(title))
        dialogo.setStandardButtons(QMessageBox.StandardButton.Ok)
        dialogo.exec()


    def startingBuckup(self):
        print(len(self.listAllFilesToCopy))
        if self.listAllFilesToCopy:
            tupleFile = self.listAllFilesToCopy[0]
            fileToCopy = tupleFile[0]
            fileNameToCopy = Utils.getFileNameByFullPathName(str(fileToCopy))
            newFile = str(self.finalPath) + str(fileNameToCopy)
            print("archivo 1 : " + fileToCopy + ", y file2 : " +newFile)
            self.copyFiles.startBackup(fileToCopy, newFile)

        self.progress_dialog = QProgressDialog(
                "Please wait while your files are being copied.",
                "Cancelar",
                0,
                0,
                self
            )
        self.progress_dialog.setWindowTitle("File Backup")
        self.progress_dialog.setWindowModality(Qt.WindowModal)
        self.progress_dialog.setMinimumDuration(0)
        self.progress_dialog.setAutoClose(False)
        self.progress_dialog.setAutoReset(False)

        self.progress_dialog.canceled.connect(self.cancelBackup)

        self.progress_dialog.show()


    def cancelBackup(self):
        # Aquí debes detener tu proceso en segundo plano
        print("Respaldo cancelado")


 #    def btn_addFilesAndFolders(self):

#        self.showAlert("Botón presionado")

#        def showAlert(self, cad):
#            QMessageBox.information(
#            self,
#            "My first alert mf",
#            cad
#            )
