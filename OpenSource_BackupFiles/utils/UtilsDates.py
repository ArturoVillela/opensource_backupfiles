# This Python file uses the following encoding: utf-8
from pathlib import Path
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QMessageBox
#from PyQt5.QtWidgets import QMessageBox
import os

class UtilsDates:
    def __init__(self):
        pass


    @staticmethod
    def isDirectoryNotEmpty(path: str)-> bool:
        """ return es directorio && tiene 0 archivos """
        return os.path.isdir(path) and len(os.listdir(path)) == 0


    @staticmethod
    def get_all_files_in_folder(ruta)-> tuple[list[str], int] :
        """ todos los archivos con full path y el size de todos. """
        listAllFiles = UtilsDates.listar_archivos_recursivos(str(ruta))
        fullSize = UtilsDates.getFullSizeOfList(listAllFiles)
        print("cant de archivos : "+str(len(listAllFiles))+ ",  full size files :" + str(fullSize))
        return listAllFiles, fullSize


    @staticmethod
    def getTuplaListFromPathList(pathList):
        listTupla : list[tuple[str, float]] = []
        for path in pathList:
            size = Path(path).stat().st_size
            listTupla.append((path, size))
        return listTupla


    @staticmethod
    def getFinalListSize(files: list[tuple[str, float]]) -> float:
        return sum(size for path, size in files)


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
        listPathsInEndFolder = UtilsDates.listar_archivos_recursivos(finalPath)
        listNamesInEndFolder = []
        listNamesInListToCopy = []
        for fullPath in listPathsInEndFolder:
            listNamesInEndFolder.append(UtilsDates.getFileNameByFullPathName(fullPath))

        for fullPath, _ in listAllNamesOfFilesToCopy:
            listNamesInListToCopy.append(UtilsDates.getFileNameByFullPathName(fullPath))

        #print("list only names of files in backup folder:")
        #Utils.printList(listNamesInListToCopy)
        print("....................................  hasta aki todo bien..")
        listConflicts = UtilsDates.indices_en_comun(listNamesInListToCopy, listNamesInEndFolder)
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
            fileName = UtilsDates.getFileNameByFullPathName(fullPath)

            if normalize(fileName) in end_set:
                indices.append(i)

        return indices if indices else None


    @staticmethod
    def indices_en_comun(listAllNamesOfFilesToCopy, listNamesInEndFolder) -> list[int]:
        listOnlyNamesInBackupList = []
        for fullPath in listAllNamesOfFilesToCopy:
            listOnlyNamesInBackupList.append(UtilsDates.getFileNameByFullPathName(fullPath))
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
        full_size:float = 0
        archivo = Path(path)
        if archivo.is_file():
            size = archivo.stat().st_size
        return size


    @staticmethod
    def listar_archivos_recursivos(ruta):
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
