# from datetime import datetime
from typing import List

from pydantic import BaseModel


class FileInfo(BaseModel):
    name: str
    size: int
    type: str


class FilePicker:
    def open_window_select(self, filters: str, path: str) -> List[FileInfo]:
        raise NotImplementedError()
