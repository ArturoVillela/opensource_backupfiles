# This Python file uses the following encoding: utf-8
from pathlib import Path
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QMessageBox
#from PyQt5.QtWidgets import QMessageBox
from data.BackUpFile import BackUpFile
from data.BackedConflictedFile import BackedConflictedFile
from datetime import datetime
from utils.FilesErrors import FilesErrors
import os

class UtilsFiles:
    def __init__(self):
        pass


    @staticmethod #subfolder, solo cuando se selecciona un folder con archivos para agregar.
    def getBackUpFileFromPath(path: str) -> BackUpFile:
        file_path = Path(path)
        file_info = file_path.stat()

#        fileNameWithSubPath = str(file_path.parent)

        return BackUpFile(
            fileName = file_path.name,
            fileNameWithPath = path,
            fileSize = file_info.st_size,
            lastDateModified = datetime.fromtimestamp(file_info.st_mtime)
        )
#

    @staticmethod
    def getBackedConflictedFileFromPath(path: str) -> BackedConflictedFile:
        file_path = Path(path)
        file_info = file_path.stat()

        fileSize = file_info.st_size
        fileName = file_path.name
        fileNameWithPath = str(file_path)
        lastDateModified = datetime.fromtimestamp(
            file_info.st_mtime
        )

        return BackedConflictedFile(
            fileName=fileName,
            fileNameWithPath=fileNameWithPath,
            fileSize=fileSize,
            lastDateModified=lastDateModified,
        )
#

    @staticmethod
    def checkForConflicts(listAllFilesToBackUp: list[BackUpFile], backupFile: BackUpFile)->str|None: #regresa el path con duplicado
        if not listAllFilesToBackUp:  #no se necesita.. pero me vale.. aki va.
            return None
        backupFileName = backupFile.fileName.lower().strip()
        for file in listAllFilesToBackUp:
            name= file.fileName.lower().strip()
            if name == backupFileName:
                return file.fileNameWithPath
        return None
#

    @staticmethod    #como usaremos un script concideraremos el name como /myfolder/b2/myfile.txt
    def getBackUpFileFromFileWithinFolder(filePath:str, folderPath:str)-> BackUpFile:
        baseFolder = Path(folderPath)
        fileFullPath = Path(filePath)
#        fileNameWithSubPath = "/" + str(fileFullPath.relative_to(baseFolder.parent))
        fileNameWithSubPath = str(fileFullPath.relative_to(baseFolder.parent))


        file_path = Path(filePath)
        file_info = file_path.stat()
        fileNameWithPath = str(file_path)

        return BackUpFile(
            file_path.name,
            filePath,
            file_info.st_size,
            datetime.fromtimestamp(file_info.st_mtime),
            fileNameWithSubPath,
            False,
            None
        )



    @staticmethod
    def getListObjects2BackupFromFolder(pathFolder:str)->list[BackUpFile]:
        listFilesInPathFolder = UtilsFiles.listar_archivos_recursivos(pathFolder)
        listFilesFromFolder: list[BackUpFile] = []
        for fullPathFile in listFilesInPathFolder:
            listFilesFromFolder.append(UtilsFiles.getBackUpFileFromFileWithinFolder(fullPathFile, pathFolder))
        return listFilesFromFolder


#
    @staticmethod
    def findConflictsInFinalPath(finalPath: str, listAllFilesToBackUp: list[BackUpFile]) -> list[BackedConflictedFile]:

        listFilesInPathFolder = UtilsFiles.listar_archivos_recursivos(finalPath)

        namesToBackUp: set[str] = set()
        for backupFile in listAllFilesToBackUp:
            namesToBackUp.add(backupFile.fileName)

        listConflicted: list[BackedConflictedFile] = []

        for path in listFilesInPathFolder:
            fileName = UtilsFiles.getFileNameByFullPathName(path)

            if fileName in namesToBackUp:
                listConflicted.append(
                    UtilsFiles.getBackedConflictedFileFromPath(path)
                )

        return listConflicted


    @staticmethod
    def isDirectoryNotEmpty(path: str)-> bool:
        """ return es directorio && tiene 0 archivos """
        return os.path.isdir(path) and len(os.listdir(path)) == 0


    @staticmethod   #Modificar, para obtener la lista de nombres desde el folder agregado
    def getAllFilePathsFromFolder(ruta, mainList:list[BackUpFile])-> list[str] | tuple[FilesErrors, str]: # lista o errores
        """ todos los archivos con full path y el size de todos. """
        listAllFiles = UtilsFiles.listar_archivos_recursivos(str(ruta))
        if not listAllFiles:
            print("folder vacio")
            return FilesErrors.EMPTY_FOLDER

        setFileNames = set()
        for full_path in listAllFiles:
            name = Path(full_path).name
            print(f"name found : {name}")

            if name in setFileNames:
                print("found duplicate in same folder")
                return FilesErrors.DUPLICATE_IN_SAME_FOLDER, name
            setFileNames.add(name)

        for backUpFile in mainList:
            if backUpFile.fileName in setFileNames:
                print("found duplicate from folder with file already added to back up")
                return FilesErrors.DUPLICATE_FILE_FOUND, backUpFile.fileName

        return listAllFiles


    @staticmethod
    def getTuplaListFromPathList(pathList):
        listTupla : list[tuple[str, float]] = []
        for path in pathList:
            size = Path(path).stat().st_size
            listTupla.append((path, size))
        return listTupla


    @staticmethod
    def getFileNameByFullPathName(full_path:str):
        return str(str(Path(full_path).name))


    @staticmethod
    def format_size(bytes_archivo):
        unidades = ["B", "KB", "MB", "GB", "TB"]
        size = float(bytes_archivo)

        for unidad in unidades:
            if size < 1024:
                return f"{size:.2f} {unidad}"

            size /= 1024

        return f"{size:.2f} PB"


    @staticmethod
    def findConflictsInBackup(listAllNamesOfFilesToCopy, finalPath) -> tuple[bool, list[int] | None]:
        """ funcion principal..listallnames contiene path y regresa indices de conflictos por nombre """
        print("....................................starting findConflicst method..")
        listPathsInEndFolder = UtilsFiles.listar_archivos_recursivos(finalPath)
        listNamesInEndFolder = []
        listNamesInListToCopy = []
        for fullPath in listPathsInEndFolder:
            listNamesInEndFolder.append(UtilsFiles.getFileNameByFullPathName(fullPath))

        for fullPath, _ in listAllNamesOfFilesToCopy:
            listNamesInListToCopy.append(UtilsFiles.getFileNameByFullPathName(fullPath))

        #print("list only names of files in backup folder:")
        #Utils.printList(listNamesInListToCopy)
        print("....................................  hasta aki todo bien..")
        listConflicts = UtilsFiles.indices_en_comun(listNamesInListToCopy, listNamesInEndFolder)
        if not listConflicts:
            print("lista vacia , no encontro conflicst")
            return False, None
        else:
            print("lista no vacia.. si encontro conflics")
            for index in listConflicts:
                print(" confliected file :",listNamesInListToCopy[index])
        return True, listConflicts


    @staticmethod
    def indices_en_comun(listAllNamesOfFilesToCopy,listNamesInEndFolder) -> list[int] | None:
        def normalize(name: str) -> str:
            return name.replace(" ", "").lower()
        end_set = {
            normalize(name)
            for name in listNamesInEndFolder
        }
        indices = []
        for i, fullPath in enumerate(listAllNamesOfFilesToCopy):
            fileName = UtilsFiles.getFileNameByFullPathName(fullPath)

            if normalize(fileName) in end_set:
                indices.append(i)

        return indices if indices else None


    @staticmethod
    def indices_en_comun(listAllNamesOfFilesToCopy, listNamesInEndFolder) -> list[int]:
        listOnlyNamesInBackupList = []
        for fullPath in listAllNamesOfFilesToCopy:
            listOnlyNamesInBackupList.append(UtilsFiles.getFileNameByFullPathName(fullPath))
        end_set = set(listNamesInEndFolder)
        return [i for i, name in enumerate(listOnlyNamesInBackupList) if name in end_set]


    @staticmethod
    def getFullSizeOfList (listPaths: list[str]) -> float:
        full_size:float = 0
        for ruta in listPaths:
            archivo = Path(ruta)
            if archivo.is_file():
                full_size += archivo.stat().st_size
        return full_size


    @staticmethod

    def getSigleFileSize (path: str) -> float:
        archivo = Path(path)
        if archivo.is_file():
            size = archivo.stat().st_size
        return size


#obtendremos la lista de archivos, pero incluyendo la ruta relativa del folder
    @staticmethod
    def getListOfAllFilesInAFolder2Backup(folderPath:str)-> list[BackUpFile]:
        file_path = Path(path)
        fileName = file_path.name

        listFullPath = [str(p) for p in Path(folderPath).rglob("*") if p.is_file()]
        #sacar los nombres
        for path in listFullPath:
            filePath = Path(path)
            fileName = filePath.name
            fileNameWithSubFolder = path.relative_to(folderPath)
            print(f"folder: {folderPath}, name:{fileName}, nameWithFolder:{fileNameWithSubFolder}")

        return
        listRelativePath: list[str] = []
        for fullPath in listFullPath:
            listRelativePath.append(fullPath.relative_to(folderPath))




    @staticmethod
    def listar_archivos_recursivos(ruta)->list[str]:
        return [str(p) for p in Path(ruta).rglob("*") if p.is_file()]


    def clearLayoutOfQScrollArea(layout:QVBoxLayout):
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
            del item


    def clearQBoxLayout(layout: QVBoxLayout) -> None:
        while layout.count() > 0:
            item = layout.takeAt(0)

            widget = item.widget()
            if widget is not None:
                widget.deleteLater()



                #                pasos a seguir para tener un scroll en un widget...
#                # 1. Crear el widget contenedor y el layout vertical
#                container_widget = QWidget()
#                v_layout = QVBoxLayout(container_widget)

#                # 2. Agregar los elementos al layout
#                v_layout.addWidget(widget_1)
#                v_layout.addWidget(widget_2)
#                # ... agregar más widgets

#                # 3. Configurar el QScrollArea
#                scroll_area = QScrollArea()
#                scroll_area.setWidgetResizable(True)  # Importante para el auto-scroll
#                scroll_area.setWidget(container_widget)

#                # 4. Establecer el scroll area como widget central o añadirlo a otro layout
#                central_widget = QWidget()
#                setCentralWidget(scroll_area)
