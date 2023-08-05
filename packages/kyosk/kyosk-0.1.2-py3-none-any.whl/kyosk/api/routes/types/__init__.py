from typing import List

from fastapi import APIRouter
from kyosk.config import config
from pydantic import BaseModel

router = APIRouter()


class Type(BaseModel):
    id: str
    name: str


@router.get("/", response_model=List[Type])
async def get_types():
    return config.api.types_allow
