# This Python file uses the following encoding: utf-8


class Resources:
    def __init__(self):
        self.listTripletaDialog: list[tuple[int, str, str]] = [
            (1,"Error", "Destination Folder not defined!"),
            (2,"Error", "No Files to backup selected"),
            (3,"Error", "Destination Folder is not empty !!"),
            (4,"Alert", "Back files Canceled by user "),
            (5,"Alert", "File Backup Completed  :) "),
            (6,"Alert", "Backup Completed Sucessfully :) "),
            (7,"Error", "Folder to backup does not contain any files!"),
            (8," Conflicts Found !!", "Click Continue to review the detected conflicts."),
            (10,"Alert", "Copy in progress....")
        ]


    def getDialogInfoByCode(self, codigo:int)->tuple[str, str]:
        for item in self.listTripletaDialog:
            if codigo == item[0]:
                return item[1], item[2]
        return None
