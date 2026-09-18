# This Python file uses the following encoding: utf-8
from pathlib import Path
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QMessageBox
#from PyQt5.QtWidgets import QMessageBox
import os

class Utils:
    def __init__(self):
        pass


    @staticmethod
    def formatear_ruta(ruta):
        lonj = 100
        mid = 43
        longitud = lonj
        if len (ruta)<= longitud:
            return ruta
        return ruta[:mid] + " .... " + ruta[-mid:]


    @staticmethod
    def formatStringWithSize(ruta, size):
        return ruta.ljust(140) + size


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
    def format_size(bytes_archivo):
        unidades = ["B", "KB", "MB", "GB", "TB"]
        size = float(bytes_archivo)

        for unidad in unidades:
            if size < 1024:
                return f"{size:.2f} {unidad}"
            size /= 1024
        return f"{size:.2f} PB"



    @staticmethod
    def getFullSizeOfList (listPaths: list[str]) -> float:
        full_size:float = 0
        for ruta in listPaths:
            archivo = Path(ruta)
            if archivo.is_file():
                full_size += archivo.stat().st_size
        return full_size


    @staticmethod
    def getDialogIconByTitle(cad:str):
        if cad == "Error":
            return QMessageBox.Icon.Warning
        elif cad == "Question":
            return QMessageBox.Icon.Question
        return QMessageBox.Icon.Information
#    QMessageBox.Icon.Information
#    QMessageBox.Icon.Warning
#    QMessageBox.Icon.Critical
#    QMessageBox.Icon.Question
#    QMessageBox.Icon.NoIcon


    def clearQBoxLayout(layout: QVBoxLayout) -> None:
        while layout.count() > 0:
            item = layout.takeAt(0)

            widget = item.widget()
            if widget is not None:
                widget.deleteLater()


    def printList(lista:list[str]) -> None:
        for word in lista:
            print(" -- ",word)

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
