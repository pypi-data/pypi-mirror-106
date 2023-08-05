import time
from enum import Enum
from typing import Dict, List, Optional

from kyosk.domain.media import MediaContainer
from pydantic import BaseModel


class MetadadoType(Enum):
    disco = "DISCO"
    card = "CARD"
    undefined = "N/A"


class KyoskMetadado(BaseModel):
    description: Optional[str] = ""
    type: MetadadoType
    media_identification: str
    workspace: str
    retranca: str


class NewTask(BaseModel):
    campaign_id: int
    media_paths: List[str]
    metadado: KyoskMetadado
    username: str


class Task(BaseModel):
    id: str
    is_finished: bool = False
    any_error: bool = False
    loaded: float = 0.0
    total: float = 0.0
    media_containers: Dict[str, MediaContainer]
    createdAt: int = int(time.time())


class Workspace(BaseModel):
    id: str
    name: str


class Type(BaseModel):
    id: str
    name: str
