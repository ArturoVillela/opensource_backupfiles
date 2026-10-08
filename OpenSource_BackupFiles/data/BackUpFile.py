# This Python file uses the following encoding: utf-8

from __future__ import annotations  #esta mmda para k me deje usar un parametro del mismo tipo...

from dataclasses import dataclass
from datetime import datetime


@dataclass
class BackUpFile:
    fileName: str
    fileNameWithPath: str
    fileSize: int
    lastDateModified: datetime
    FileNameWithSubPath: str | None = None #nombre del archivo cuando viene de un folder
    conflicted: bool = False  # solo para folder end path donde se pondra el respaldo
    conflictedFiles: list[BackUpFile] | None = None




