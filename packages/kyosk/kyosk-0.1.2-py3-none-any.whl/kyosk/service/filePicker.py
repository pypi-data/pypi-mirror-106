from contextlib import contextmanager
from os import name as OS_NAME
from pathlib import Path
from threading import Lock
from typing import List

from kyosk.service.interface.file_picker_interface import FileInfo
from kyosk.service.interface.file_picker_interface import (
    FilePicker as FilePickerInterface,
)
from kyosk.util import get_mimetype

file_chooser_lock = Lock()


def os_filechooser(initial_dir: str, title: str, ext_filter: str):
    if OS_NAME == "nt":
        return winapi_filechooser(initial_dir, title, ext_filter)
    else:
        return tkinter_filechooser(initial_dir, title, ext_filter)


def tkinter_filechooser(initial_dir: str, title: str, ext_filter: str):
    from tkinter import Tk
    from tkinter.filedialog import askopenfilenames

    root = Tk()
    root.withdraw()
    root.wm_attributes("-topmost", 1)

    if ext_filter != "":
        file_paths = askopenfilenames(
            initialdir=initial_dir,
            title=title,
            filetypes=map(lambda s: ("", "*" + s.strip()), ext_filter.split(",")),
        )
    else:
        file_paths = askopenfilenames(initialdir=initial_dir, title=title)
    root.destroy()
    return file_paths


@contextmanager
def window():
    import win32gui
    import win32api
    import win32con

    window_handle = win32gui.CreateWindowEx(
        win32con.WS_EX_TOPMOST,
        "BUTTON",
        "",
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        win32api.GetModuleHandle(None),
        None,
    )
    try:
        yield window_handle
    finally:
        win32gui.DestroyWindow(window_handle)


def winapi_filechooser(initial_dir: str, title: str, ext_filter: str):
    import win32con
    import win32gui

    # import ctypes

    with window() as window_handle:
        flags = (
            win32con.OFN_ALLOWMULTISELECT
            | win32con.OFN_EXPLORER
            | win32con.OFN_PATHMUSTEXIST
            | win32con.OFN_FILEMUSTEXIST
        )
        try:
            if ext_filter != "":
                # .mpeg, .mp4, .ogg, .webm, .mov
                # mpeg, mp4, ogg, webm, mov\0*.mpeg;*.mp4;*.ogg;*.webm;*.mov;*.avi;*.mp3;*.oga;*.wav;*.opus;*.aac;*.m4a;*.amr;*.png;*.jpeg;*.jpg;*.gif
                win_filter = (
                    ext_filter.replace(".", "")
                    + "\0"
                    + ext_filter.replace(".", "*.").replace(", ", ";")
                    + "\0"
                )
                results = win32gui.GetOpenFileNameW(
                    hwndOwner=window_handle,
                    InitialDir=initial_dir,
                    Title=title,
                    MaxFile=1024 * 1024,
                    Filter=win_filter,
                    Flags=flags,
                )[0]
            else:
                results = win32gui.GetOpenFileNameW(
                    hwndOwner=window_handle,
                    InitialDir=initial_dir,
                    Title=title,
                    MaxFile=1024 * 1024,
                    Flags=flags,
                )[0]
        except win32gui.error:
            return []

    results_parts = results.split("\x00")
    if len(results_parts) == 1:
        return results_parts
    else:
        dir_path, *files = results_parts
        file_paths = [str(Path(dir_path) / file) for file in files]
        return file_paths


class FilePicker(FilePickerInterface):
    def open_window_select(self, filters: str, path: str) -> List[FileInfo]:
        file_chooser_lock.acquire()
        file_paths = os_filechooser(
            path, "Selecione os arquivos para a transferência", filters
        )
        file_chooser_lock.release()
        files = []
        for path in file_paths:
            mime_type = get_mimetype(path)
            _path = Path(path)
            files.append(
                FileInfo(
                    name=str(_path.absolute()),
                    size=_path.stat().st_size,
                    type=mime_type,
                )
            )

        return files
