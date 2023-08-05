import mimetypes
from pathlib import Path

mimetypes.init()


def get_mimetype(path_to_file: str) -> str:
    _path = Path(path_to_file)
    try:
        return mimetypes.types_map[_path.suffix.lower()]
    except KeyError:
        return "application/octet-stream"
