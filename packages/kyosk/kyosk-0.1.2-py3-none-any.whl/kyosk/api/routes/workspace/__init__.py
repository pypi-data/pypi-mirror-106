from typing import List

from fastapi import APIRouter
from kyosk.config import config
from pydantic import BaseModel

router = APIRouter()


class Workspace(BaseModel):
    id: str
    name: str


@router.get("/", response_model=List[Workspace])
async def get_workspace():
    return config.api.workspace_allow
