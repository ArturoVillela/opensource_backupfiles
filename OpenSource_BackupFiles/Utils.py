# This Python file uses the following encoding: utf-8
from pathlib import Path

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
    def get_all_files_in_folder(ruta):
        files = Utils.listar_archivos_recursivos(str(ruta))
        fullSize = Utils.getFullSizeOfList(files)
        print("cant de archivos : "+str(len(files))+ ",  full size files :" + str(fullSize))
        return files, fullSize


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


    def listar_archivos_recursivos(ruta):
        # rglob("*") devuelve todos los archivos y carpetas
        # is_file() filtra para incluir solo archivos
        return [str(p) for p in Path(ruta).rglob("*") if p.is_file()]
