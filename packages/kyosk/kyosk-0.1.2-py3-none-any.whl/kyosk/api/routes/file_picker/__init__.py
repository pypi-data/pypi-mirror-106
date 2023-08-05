from fastapi import APIRouter, Depends, Query
from kyosk.api.controller.file_picker.file_picker_controller import FilePickerController
from kyosk.api.controller.file_picker.schema import FilePickerOut

router = APIRouter()


@router.get("/{campaign_id}", response_model=FilePickerOut)
async def open_file_picker(
    campaign_id: int,
    filters: str = Query(""),
    path: str = Query(""),
    file_picker_controller: FilePickerController = Depends(),
):
    return await file_picker_controller.pick_files(
        campaign_id=campaign_id, filters=filters, path=path
    )
