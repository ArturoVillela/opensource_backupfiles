# This Python file uses the following encoding: utf-8

from PySide6.QtCore import QProcess, QObject, Signal


class CopyFiles(QObject):

    backupCompleted = Signal()   #emit es programacion reactiva
    backupFailed = Signal(str)


    def __init__(self, parent = None):
        super().__init__(parent)
        self.backup_process = None


    def startBackup(self, origen, destino):
        self.backup_process = QProcess(self)

        self.backup_process.finished.connect(self.backupFinished)
        self.backup_process.errorOccurred.connect(self.backupError)

        self.backup_process.start(
            "/home/charlito/Documents/dev/python/script/copyScript.sh",
            [origen, destino]
        )


    def backupFinished(self, exit_code, exit_status):
        print("Proceso terminado:", exit_code)
        if exit_code == 0:
            self.backupCompleted.emit()
        else:
            error = self.backup_process.readAllStandardError().data().decode()
            self.backupFailed.emit(error or f"El script terminó con código {exit_code}")


    def backupError(self, error):
        print("Error ejecutando el respaldo:", error)
        self.backupFailed.emit(
            f"No se pudo ejecutar el respaldo: {error}"
        )

    def cancelBackup(self):
        if self.backup_process.state() != QProcess.NotRunning:
            self.backup_process.terminate()
