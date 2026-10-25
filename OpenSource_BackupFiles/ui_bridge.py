from PySide6.QtWidgets import QMainWindow
from base19_ui import Ui_MainWindow
from pathlib import Path
from PySide6 import QtCore
from Resources import Resources
from PySide6.QtCore import QObject, QThread, Signal, Qt
from PySide6.QtWidgets import QProgressDialog
import json

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
from data.BackedConflictedFile import BackedConflictedFile
from utils.FilesErrors import FilesErrors
#import os


class UiBridge(QMainWindow):

    def __init__(self):
        super().__init__()

        self.listPathsDir: list[str] = []
        self.listAllFilesToCopy: list[tuple[str, float]] = []
        self.listAllNamesOfFilesToCopy: list[str]
        self.listAllFilesToBackUp: list[BackUpFile] = []    #esta es la lista de archivos a copiar
        self.listAddedFoldersPath: list[str] = []

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
        self.ui.btnCancelScrn2.clicked.connect(self.btnCancelScrn2Clicked)
#       falta agregar las funciones de estos botones
        self.ui.btnSkipAll.clicked.connect(self.btnSkipAllClicked)
        self.ui.btnOverwritteAll.clicked.connect(self.btnOverwritteAllClicked)
#        self.ui.btnSolveConflicts.clicked.connect(self.btnSolveConflictsClicked)
#        en segunda pantalla el btn start se llama btnSolveConflicts

    def btnSkipAllClicked(self):
        self.webView2.page().runJavaScript("setAllActions('skip');")

#
    def btnOverwritteAllClicked(self):
        self.webView2.page().runJavaScript("setAllActions('overwrite');")

#
    def initSecondScreen(self):
        cantConflicts = UtilsFiles.getCantConflicts(self.listAllFilesToBackUp)
        self.cambiarPantalla(2)
        self.updateLabelConflicts(cantConflicts)
        self.addRowToSecondTable()

#
    def updateLabelConflicts(self, cantConflicts: int):
        self.ui.labelXConflics.setText(f"files with conflicts : {cantConflicts}")

#
    def btnCancelScrn2Clicked(self):
        self.restarWebViewSecondScreen()
        self.cambiarPantalla(1)


#
    def btnStartClicked(self):
        if not self.listAllFilesToBackUp:
            self.showAlertByDialogCode(2)
            return
        if not self.finalPath:
            self.showAlertByDialogCode(1)
            return
        conflictedFound = UtilsFiles.findConflictsInFinalPath2(self.finalPath, self.listAllFilesToBackUp)
        if conflictedFound:
            self.initSecondScreen()
            return
        self.startingBackup2()

#
    def btnClearAllClicked(self):
        self.listAllFilesToBackUp.clear()
        self.updateLabelInfo()
        self.ui.label_all_files_to_copy.setText (" ")
        self.initWebView()

#
    def btnAddFilesToBackupClicked(self):
        ruta = self.seleccionar_ruta()
        if ruta:
            backupFile = UtilsFiles.getBackUpFileFromPath(ruta)
            pathFileConflicted = UtilsFiles.checkForConflicts(self.listAllFilesToBackUp, backupFile)
            print("pathFileConflicte : ",pathFileConflicted)
            if pathFileConflicted is not None:  # si no es None, tiene la ruta del error
                cad = str(f"File already selected to backup\n<<{backupFile.fileName}>>\n Unable to add the file")
                self.showAlertByDialogCode(9,cad)
                return
            else:
                print("no conflicts found")
        self.listAllFilesToBackUp.append(backupFile)
        ruta2 = Utils.formatear_ruta(backupFile.fileNameWithPath)
        formated_size = Utils.format_size(backupFile.fileSize)
        self.addRowToTable(ruta2, formated_size)
        self.updateLabelInfo()

#
    def btnAddFoldersToBackupClicked(self):
        ruta = self.seleccionarFolder()
        if ruta is None:
            return
        for folderAdded in self.listAddedFoldersPath:
            if folderAdded == ruta:
                self.showAlertByDialogCode(13)
                return
            if Path(ruta).resolve().is_relative_to(Path(folderAdded).resolve()):
                self.showAlertByDialogCode(14,f"This folder is already selected for backup in \n\n{folderAdded}")
                return
            if Path(folderAdded).resolve().is_relative_to(Path(ruta).resolve()):
                self.showAlertByDialogCode(14,f"This folder generate a conflics with previously added folder:\n\n{ruta}")
                return
        self.listAddedFoldersPath.append(ruta)
        listObjectsInFolder = UtilsFiles.getListObjects2BackupFromFolder(ruta)
        if not listObjectsInFolder:
            self.showAlertByDialogCode(7)
            print("folder seleccionado esta vacio")
            return
        self.listAllFilesToBackUp.extend(listObjectsInFolder)
        folderSize: float = 0
        for obj in listObjectsInFolder:
            folderSize += obj.fileSize
        sizeFormated = Utils.format_size(folderSize)
        ruta2 = Utils.formatear_ruta(ruta)
        print(f"El folder seleccionada es: {ruta2}, \nSe muestra:{ruta}")
        self.addRowToTable(ruta2, sizeFormated)
        self.updateLabelInfo()

#
    def btnSelectEndFolderClicked(self): #pone la ruta final donde se hara el respaldo
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

#
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

#
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

#
    def updateLabelInfo(self):
        cantFiles = len(self.listAllFilesToBackUp)
        if cantFiles > 0:
            fullSize = Utils.getFinalListSize(self.listAllFilesToBackUp)
            formatedSize = Utils.format_size(fullSize)
            self.ui.label_all_files_to_copy.setText (f"Cant files:{cantFiles}, Size :{formatedSize} " )
        else:
            self.ui.label_all_files_to_copy.setText (" ")

#
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

#
    def startingBackup2(self):
        total = len(self.listAllFilesToBackUp)
        print("starting backup files main function......cant files: ",total)

#        ###### por el momento ignoramos este check para la segunda pantalla....
#        if not UtilsFiles.isDirectoryNotEmpty(self.finalPath):
#            """ no esta vacio el end directory... """
#            # Utils.printList(self.listAllFilesToCopy)   listAllFilesToCopy
#            conflictsFound, listIndexWithConflicts = UtilsFiles.findConflictsInBackup(self.listAllFilesToCopy, self.finalPath)
#            if conflictsFound:
#                print(f"encontramos {len(listIndexWithConflicts)} conflictos")
#                print("lo que sigue es lanzar la otra screen....")
#                self.listIndexsWithConflicts = listIndexWithConflicts
#                self.requestConfirmationForConflicsts()
#                return
        ###### por el momento ignoramos este check para la segunda pantalla....
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
            objToCopy = self.listAllFilesToBackUp.pop(0)
            if self.progress_dialog.wasCanceled():
                return

#            print(f"primer archivo seleccionado : {objToCopy.fileNameWithPath}")
#            print(f"objToCopy is type of :{objToCopy}")
            fileDestino = objToCopy.fileNameWithSubPath if objToCopy.fileNameWithSubPath is not None else objToCopy.fileName
            print(f"archivo a copiar: {fileDestino}")

            #fileNameToCopy = objToCopy.source_file_pathWithName
            croppedFileName = Utils.formatear_ruta(fileDestino)
#            newFile = str(self.finalPath) +"/"+ str(objToCopy.source_file_name) respaldo lda
            newFile = str(self.finalPath) +"/"+ fileDestino
            print(f"new file rute: {newFile}")
            filesLeftToCopy = len(self.listAllFilesToCopy)
            self.progress_dialog.setLabelText(
                f"Please wait: copying {croppedFileName}\nFiles left to copy: {filesLeftToCopy}"
            )
            print(f"trataremos de copiar:::>  {objToCopy.fileNameWithPath}, y nuevo archivo en : {newFile}")
            Path(newFile).parent.mkdir(parents=True, exist_ok=True)
            self.copyFiles.startBackup(objToCopy.fileNameWithPath, newFile)  #origen y destino
        else:
            self.progress_dialog.close()
            self.isBackupStarted = False
            self.showAlertByDialogCode(2)


    def cancelBackup(self):
        self.progress_dialog.hide()
        self.copyFiles.cancelBackup()
        self.showAlertByDialogCode(4)

#
    def onBackupCompleted(self):
        print("......backup completed of a single file.. and got the result on ui_bridge")
        cantFilesLeft = len(self.listAllFilesToBackUp)
        print("cant de archivos a copiar: "+str(cantFilesLeft))
        if self.listAllFilesToBackUp:
            self.progress_dialog.hide()
            self.startingBackup2()
        else:
            self.restarFirstScreen(True)

#
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

#
    def restarFirstScreen(self, completed:bool = False):
        self.progress_dialog.hide()
        self.isBackupStarted = False
        self.listAllFilesToBackUp.clear()
        self.restarTable()
        self.updateLabelInfo()
        self.finalPath = ""
        self.ui.etToFolder.setText("/...")
        self.listAddedFoldersPath.clear()
        if (completed):
            self.showAlertByDialogCode(6)


#
    def onBackupError(self, error_msg):
        print("backup error... on bridge class")
        self.btnClearAllClicked()
        if self.progress_dialog:
            self.progress_dialog.hide()
        self.showAlertByDialogCode(12)

#
    def cambiarPantalla(self, index:int) ->None:
        if index == 1:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_1)
            self.currentScreenSelected = 1
            self.ui.btn_start.setText (" Solve Conflicts ")
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
            self.currentScreenSelected = 2

#
    def initWebView(self):
        htmlPath = Path("html/nocheckbox.html")
        with open(htmlPath, "r", encoding="utf-8") as file:
            htmlPage = file.read()
        self.webView.setHtml(htmlPage)
        self.initWebViewSecondPage()

#
    def initWebViewSecondPage(self):
        htmlPath = Path("html/selector2.html")
        with open(htmlPath, "r", encoding="utf-8") as file:
            htmlPage = file.read()
        self.webView2.setHtml(htmlPage)


#
    def addRowToTable(self, str1, str2):
        script = f"addRowToTable('{str1}', '{str2}')"
        self.webView.page().runJavaScript(script)

#
    def restarWebViewSecondScreen(self):
        script = (
            f"restarWebViewSecondScreen();"
        )
        self.webView2.page().runJavaScript(script)


#
    def addRowToSecondTable(self):
        print("psss si llega al add row to sendo table....")
        for index, obj in enumerate(self.listAllFilesToBackUp):
#        for obj in self.listAllFilesToBackUp:
            print(f"obj nombre:{obj.fileName}, conflicted: {obj.conflictedFile}")
            if obj.conflictedFile is None : continue
            nameOnly = obj.fileName
            formattedPath = Utils.formatearRutaForConflicts(obj.fileNameWithPath)
            fileSize = Utils.format_size(obj.fileSize)
            dateModified = obj.getDateAsStr()
            nameOnly = nameOnly+ f" index->{index} "
            script = (
                f"addRowToTable3("
                f"{json.dumps(nameOnly)}, "
                f"{json.dumps(formattedPath)}, "
                f"{json.dumps(fileSize)}, "
                f"{json.dumps(dateModified)}, "
                f"{json.dumps(index)}, "
                f");"
            )
            self.webView2.page().runJavaScript(script)

#
    def restarTable(self):
        script2 = f"clearTable()"
        self.webView.page().runJavaScript(script2)

#
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
