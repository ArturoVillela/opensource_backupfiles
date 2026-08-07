# This Python file uses the following encoding: utf-8


class Utils:
    def __init__(self):
        pass


    @staticmethod
    def formatear_ruta(ruta):
        longitud = 33
        if len (ruta)<= longitud:
            return ruta

        return ruta[:15] + " ... " + ruta[-15:]
