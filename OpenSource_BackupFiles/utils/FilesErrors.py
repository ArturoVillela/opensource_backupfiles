# This Python file uses the following encoding: utf-8
from enum import Enum, auto


class FilesErrors(Enum):
    EMPTY_FOLDER = auto()
    DUPLICATE_IN_SAME_FOLDER = auto()
    DUPLICATE_FILE_FOUND = auto()
