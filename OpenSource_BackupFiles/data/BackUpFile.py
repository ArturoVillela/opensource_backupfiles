# This Python file uses the following encoding: utf-8

from dataclasses import dataclass
from datetime import datetime


@dataclass
class BackUpFile:
    source_file_name: str
    source_file_pathWithName: str
    source_file_pathWithoutName: str
    source_file_size: int
    source_last_date_modified: datetime
    root_folder: str | None





