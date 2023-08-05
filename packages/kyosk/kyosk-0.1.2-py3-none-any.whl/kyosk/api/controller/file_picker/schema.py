from typing import List

from pydantic import BaseModel


class File(BaseModel):
    name: str
    size: int
    type: str


class Sftp(BaseModel):
    host: str
    path: str


class FilePickerOut(BaseModel):
    files: List[File]
    sftp: Sftp
