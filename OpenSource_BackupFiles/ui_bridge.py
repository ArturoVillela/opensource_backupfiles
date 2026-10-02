from PySide6.QtWidgets import QMainWindow
from base17_ui import Ui_MainWindow
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
from utils.Utils import Utils
from utils.UtilsFiles import UtilsFiles
from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout
from CopyFiles import CopyFiles
from data.BackUpFile import BackUpFile
from utils.FilesErrors import FilesErrors
#import os


class UiBridge(QMainWindow):

    def __init__(self):
        super().__init__()

        self.listPathsDir: list[str] = []
        self.listAllFilesToCopy: list[tuple[str, float]] = []
        self.listAllNamesOfFilesToCopy: list[str]
        self.listAllFilesToBackUp: list[BackUpFile] = []    #esta es la lista de archivos a copiar


        self.listIndexsWithConflicts: list[int] = []
        self.finalPath: str = ""
        self.currentScreenSelected = 1

        self.copyFiles = CopyFiles()
        self.progress_dialog = None

        self.isBackupStarted: bool = False
        self.isBackupFailed: bool = False

        self.copyFiles.backupCompleted.connect(self.onBackupCompleted) #listeners reactive programming for script
        self.copyFiles.backupFailed.connect(self.onBackupFailed)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.containerLayout = self.ui.scrollAreaWidgetContents.layout()
        print(type(self.containerLayout))
        self.conectar_eventos()

        self.webView = self.ui.widgetWebView
        self.webView2 = self.ui.widgetWebView2
        self.htmlPage = ""
        self.initWebView()


    def conectar_eventos(self):
        self.ui.btnAddFilesToSave.clicked.connect(self.btnAddFilesToBackupClicked)
        self.ui.btnAddFolders.clicked.connect(self.btnAddFoldersToBackupClicked)
        self.ui.btnSelectToFolder.clicked.connect(self.btnSelectEndFolderClicked)
        self.ui.btn_clear_all.clicked.connect(self.btnClearAllClicked)
        self.ui.btn_start.clicked.connect(self.btnStartClicked)


    def initWebView(self):
        htmlPath = Path("html/nocheckbox.html")
        with open(htmlPath, "r", encoding="utf-8") as file:
            htmlPage = file.read()
        self.webView.setHtml(htmlPage)


    def initWebViewSecondPage(self):
        htmlPath = Path("html/selector.html")
        with open(htmlPath, "r", encoding="utf-8") as file:
            htmlPage = file.read()
        self.webView2.setHtml(htmlPage)


    def btnStartClicked(self):
        if not self.listAllFilesToBackUp:
            self.showAlertByDialogCode(2)
            return
        if not self.finalPath:
            self.showAlertByDialogCode(1)
            return
        if not UtilsFiles.isDirectoryNotEmpty(self.finalPath):
            # self.showAlertByDialogCode(3)
            reply = QMessageBox.question(
                    self,
                    "Confirm",
                    "Folder Selected is not empyt, proceed? ",
                    QMessageBox.Ok | QMessageBox.Cancel,
                    QMessageBox.Cancel  # botón por defecto (focus)
                )
            if reply != QMessageBox.Ok:
                return
        self.startingBackup2()


    def btnClearAllClicked(self):
        self.listAllFilesToBackUp.clear()
        self.updateLabelInfo()
        self.ui.label_all_files_to_copy.setText (" ")
        self.initWebView()
        print("aki limpiamos el layout de archivos, nuevo size : " +str(len(self.listAllFilesToCopy)))


    def btnAddFilesToBackupClicked(self):
        ruta = self.seleccionar_ruta()
        if ruta:
            backupFile = UtilsFiles.getBackUpFileFromPath(ruta)
            pathFileConflicted = UtilsFiles.checkForConflicts(self.listAllFilesToBackUp, backupFile)
            print("pathFileConflicte : ",pathFileConflicted)
        if pathFileConflicted:  # si no es None, tiene la ruta del error
            cad = str(f"File already selected to backup\n<<{backupFile.source_file_name}>>\n Unable to add the file")
            self.showAlertByDialogCode(9,cad)
            return
        self.listAllFilesToBackUp.append(backupFile)

        ruta2 = Utils.formatear_ruta(backupFile.source_file_pathWithName)
        formated_size = Utils.format_size(backupFile.source_file_size)
        self.addRowToTable(ruta2,formated_size)
        self.updateLabelInfo()

    def btnAddFoldersToBackupClicked(self):
        ruta = self.seleccionarFolder()
        print (f"ruta = {ruta}")
        if ruta is None:
            return
        listFullPathFilesToAddFromFolder = UtilsFiles.getAllFilePathsFromFolder(ruta, self.listAllFilesToBackUp)

        if isinstance(listFullPathFilesToAddFromFolder, FilesErrors):
            self.showAlertByDialogCode(11)
            return

        if not listFullPathFilesToAddFromFolder:
            self.showAlertByDialogCode(7)
            print("folder seleccionado esta vacio")
            return

        print("las pruebas llegan hasta aki.. a probar esta madre...")
        #lo que sigue es crear la lista de objetos
        #usar UtilsFiles.getBackUpFileFromPath(ruta)
        #self.listAllFilesToBackUp: list[BackUpFile] = []
        folderSize : float = 0
        for path in listFullPathFilesToAddFromFolder:
            backUpObject = UtilsFiles.getBackUpFileFromPath(path, ruta)
            self.listAllFilesToBackUp.append(backUpObject)
            folderSize += backUpObject.source_file_size

        #sigue sacar el full size of list of objects
        sizeFormated = Utils.format_size(folderSize)
        ruta2 = Utils.formatear_ruta(ruta)
        print(f"El folder seleccionada es: {ruta2}, \nSe muestra:{ruta}")
        self.addRowToTable(ruta2, sizeFormated)
        self.updateLabelInfo()


    def btnSelectEndFolderClicked(self):
        ruta = self.seleccionarFolder()
        self.isBackupFolderEmpty = True
        if ruta is None:
            return
        if not UtilsFiles.isDirectoryNotEmpty(ruta):
            reply = QMessageBox.question(
                    self,
                    "Confirm",
                    "Folder Selected is not empyt, proceed? ",
                    QMessageBox.Ok | QMessageBox.Cancel,
                    QMessageBox.Cancel  # botón por defecto (focus)
                )
            if reply != QMessageBox.Ok:
                return
        self.finalPath = ruta
        rutaFormatted = Utils.formatear_ruta(ruta)
        self.ui.etToFolder.setText(rutaFormatted)


    def seleccionar_ruta(self):
        opciones = QFileDialog.Option.DontUseNativeDialog
        dialogo = QFileDialog(self)
        dialogo.setWindowTitle("Selecciona un archivo")
        dialogo.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialogo.setOptions(opciones)
        if dialogo.exec():
            rutas = dialogo.selectedFiles()
            if rutas:
                return rutas[0]
            return None


    def seleccionarFolder(self):
        opciones = QFileDialog.Option.DontUseNativeDialog
        dialog = QFileDialog(self)
        dialog.setOptions(opciones)
        dialog.setWindowTitle("Selecciona una carpeta")
        dialog.setFileMode(QFileDialog.FileMode.Directory)

        if dialog.exec():
            rutas = dialog.selectedFiles()
            if rutas:
                return rutas[0]
        return None


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
                | QtCore.Qt.AlignmentFlag.AlignVCenter)

        label_size = QLabel(size)
        label_size.setFixedWidth(200)
        label_size.setStyleSheet("border: none;")

        row_layout.addWidget(label_ruta)
        row_layout.addWidget(label_size)
        self.containerLayout.addWidget(label_ruta)


    def updateLabelInfo(self):
        fullSize = Utils.getFinalListSize(self.listAllFilesToBackUp)
        cantFiles = len(self.listAllFilesToBackUp)
        formatedSize = Utils.format_size(fullSize)
        self.ui.label_all_files_to_copy.setText (f"Cant files:{cantFiles}, Size :{formatedSize} " )


    def showAlertByDialogCode(self, code:int, forcedSubtitle:str = None) -> None:
        dialogo = QMessageBox(self)
        title, subtitle = Resources().getDialogInfoByCode(code)
        dialogo.setWindowTitle(title)
        if forcedSubtitle:
            subtitle = forcedSubtitle
        dialogo.setText(subtitle)
        dialogo.setIcon(Utils.getDialogIconByTitle(title))
        #dialogo.setStandardButtons(QMessageBox.StandardButton.Ok)
        dialogo.exec()


#        self.listAllFilesToCopy: list[tuple[str, float]] = []
#        self.listAllNamesOfFilesToCopy: list[str]
#        self.listAllFilesInEndDirectory : list[tuple[str, str]]

    def startingBackup2(self):
        total = len(self.listAllFilesToBackUp)
        #print("\n" * 60)  # empuja el contenido anterior fuera de la pantalla    # limpia la pantalla visible
        print("starting backup files main function......cant files: ",total)
        if not UtilsFiles.isDirectoryNotEmpty(self.finalPath):
            """ no esta vacio el end directory... """
            # Utils.printList(self.listAllFilesToCopy)   listAllFilesToCopy
            conflictsFound, listIndexWithConflicts = UtilsFiles.findConflictsInBackup(self.listAllFilesToCopy, self.finalPath)
            if conflictsFound:
                print(f"encontramos {len(listIndexWithConflicts)} conflictos")
                print("lo que sigue es lanzar la otra screen....")
                self.listIndexsWithConflicts = listIndexWithConflicts
                self.requestConfirmationForConflicsts()
                return
#            else:
#                print("no encontro conflictos...")
#            return
#        else:   # este else evita termina el copiado antes de copiar archivos, usado para no copiar por error.
#            print("por el momento solo checaremos cuando el end folder tiene files.. ending program")
#            return
        #por el momento no se llega a las lineas siguientes...
        if not self.isBackupStarted:  # solo inicializa el progress dialog
            print("entra al check for self.isBackupStarted")
            self.progress_dialog = QProgressDialog(
                "Please wait:",
                "Cancelar",
                0, 0, self
            )
            self.progress_dialog.setWindowTitle("File Backup")
            self.progress_dialog.setWindowModality(Qt.WindowModal)
            self.progress_dialog.setMinimumDuration(0)
            self.progress_dialog.setAutoClose(True)
            self.progress_dialog.setAutoReset(False)
            self.progress_dialog.canceled.connect(self.cancelBackup)
#            self.progress_dialog.show()
            self.isBackupStarted = True

        if self.listAllFilesToBackUp:
            print("entra al check for self.listAllFilesToBackUp, aki devemos chekar por conflictos..")
            self.progress_dialog.show()
#            duplaPathSize = self.listAllFilesToCopy.pop(0)
            objToCopy = self.listAllFilesToBackUp.pop(0)
            if self.progress_dialog.wasCanceled():
                return

            fileNameToCopy = objToCopy.source_file_pathWithName
            croppedFileName = Utils.formatear_ruta(fileNameToCopy)
            newFile = str(self.finalPath) +"/"+ str(objToCopy.source_file_name)
            filesLeftToCopy = len(self.listAllFilesToCopy)
            self.progress_dialog.setLabelText(
                f"Please wait: copying {croppedFileName}\nFiles left to copy: {filesLeftToCopy}"
            )
            print(f"archivo : {fileNameToCopy}, y file2 : {newFile}")
            self.copyFiles.startBackup(fileNameToCopy, newFile)
        else:
            self.progress_dialog.close()
            self.isBackupStarted = False
            self.showAlertByDialogCode(2)


    def cancelBackup(self):
        self.progress_dialog.hide()
        self.copyFiles.cancelBackup()
        self.showAlertByDialogCode(4)


    def onBackupCompleted(self):
        print("......backup completed of a single file.. and got the result on ui_bridge")
        cantFilesLeft = len(self.listAllFilesToBackUp)
        print("cant de archivos a copiar: "+str(cantFilesLeft))
        if self.listAllFilesToBackUp:
            self.progress_dialog.hide()
            self.startingBackup2()
        else:
            self.progress_dialog.hide()
            self.isBackupStarted = False
            self.showAlertByDialogCode(6)

    def onBackupFailed(self, error_message):     #TODO utilizar el sistema de dialogos predefinido en lugar de un critical
        print("backup completed w/error.. and got the result on ui bridge")
        if self.progress_dialog:
            self.progress_dialog.hide()

        QMessageBox.critical(
            self,
            "Error",
            error_message
        )
        self.btnClearAllClicked()


    def onBackupError(self, error_msg):
        print("backup error... on bridge class")
        self.btnClearAllClicked()
        if self.progress_dialog:
            self.progress_dialog.hide()
        self.showAlertByDialogCode(12)


    def cambiarPantalla(self, index:int) ->None:
        if index == 1:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_1)
            currentScreenSelected = 1
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
            currentScreenSelected = 2


    def addRowToTable(self, str1, str2):
        script = f"addRowToTable('{str1}', '{str2}')"
        self.webView.page().runJavaScript(script)


    def requestConfirmationForConflicsts(self):
        dialogo = QMessageBox(self)
        title, subtitle = Resources().getDialogInfoByCode(8)
        dialogo.setWindowTitle(title)
        dialogo.setText(subtitle)
        dialogo.addButton("Cancel", QMessageBox.RejectRole)
        btn_ok = dialogo.addButton("Continue", QMessageBox.YesRole)

        dialogo.setDefaultButton(btn_ok)
        dialogo.exec()
        if dialogo.clickedButton() == btn_ok:
            self.cambiarPantalla(2)
            self.initWebViewSecondPage()
            print("clicked btn ok")
