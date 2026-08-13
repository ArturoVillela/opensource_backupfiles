# This Python file uses the following encoding: utf-8
from pathlib import Path

class Utils:
    def __init__(self):
        pass


    @staticmethod
    def formatear_ruta(ruta):
        longitud = 33
        if len (ruta)<= longitud:
            return ruta

        return ruta[:15] + " ... " + ruta[-15:]


    @staticmethod
    def get_all_files_in_folder(ruta):
        archivos = Utils.listar_archivos_recursivos(str(ruta))
        print("cant de archivos : "+str(len(archivos)))
        return archivos


    @staticmethod
    def format_size(bytes_archivo):
        unidades = ["B", "KB", "MB", "GB", "TB"]
        tamanio = float(bytes_archivo)

        for unidad in unidades:
            if tamanio < 1024:
                return f"{tamanio:.2f} {unidad}"

            tamanio /= 1024

        return f"{tamanio:.2f} PB"


    def listar_archivos_recursivos(ruta):
        # rglob("*") devuelve todos los archivos y carpetas
        # is_file() filtra para incluir solo archivos
        return [str(p) for p in Path(ruta).rglob("*") if p.is_file()]
