from kyosk.service.colaborativo import ColaborativoService
from kyosk.service.filePicker import FilePicker
from kyosk.service.interface.file_picker_interface import (
    FilePicker as FilePickerInterface,
)

from .schema import FilePickerOut

_colaborativo_service = ColaborativoService()
_file_picker = FilePicker()


class FilePickerController:
    async def pick_files(
        self,
        campaign_id: int,
        filters: str,
        path: str,
        file_picker: FilePickerInterface = _file_picker,
    ) -> FilePickerOut:
        sftp_credentials = await _colaborativo_service.get_sftp_credentials(campaign_id)
        files = file_picker.open_window_select(filters=filters, path=path)
        return FilePickerOut(sftp=sftp_credentials.simple_info(), files=files,)
