# This Python file uses the following encoding: utf-8
from dataclasses import dataclass
from datetime import datetime

@dataclass
class BackedConflictedFile:
    source_file_name: str
    source_file_pathWithName: str
    source_file_size: int = 0
    source_last_date_modified: datetime | None = None

    def getDateAsStr(self) -> str:
        return self.source_last_date_modified.strftime('%Y-%m-%d %H:%M')
