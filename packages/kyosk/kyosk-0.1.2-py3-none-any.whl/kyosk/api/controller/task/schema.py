import time
from enum import Enum
from typing import Dict, List, Optional

from pydantic import BaseModel, confloat


class MediaStatus(Enum):
    pending = "pending"
    processing = "processing"
    success = "success"
    rename = "rename"
    error = "error"


class MetadadoType(Enum):
    disco = "DISCO"
    card = "CARD"
    undefined = "N/A"


class Metadata(BaseModel):
    description: Optional[str] = ""
    type: MetadadoType
    media_identification: str
    workspace: str
    retranca: str


class TaskIn(BaseModel):
    campaign_id: int
    media_paths: List[str]
    metadado: Metadata
    username: str


class MediaOut(BaseModel):
    name: str
    path: str
    mimetype: str
    size: int
    sent: int = 0
    complete_percentage: confloat(ge=0.0, le=100.0) = 0.0
    status: MediaStatus = MediaStatus.pending


class XmlOut(BaseModel):
    id: str
    filename: str
    datetime: str
    retranca: str
    description: Optional[str] = ""
    card: str
    workspace: str  # campaign's name
    username: str
    status: MediaStatus = MediaStatus.pending


class MediaContainerOut(BaseModel):
    id: str
    media: MediaOut
    xml: XmlOut


class TaskOut(BaseModel):
    id: str
    is_finished: bool = False
    any_error: bool = False
    loaded: float = 0.0
    total: float = 0.0
    media_containers: Dict[str, MediaContainerOut]
    createdAt: int = int(time.time())


class WorkspaceOut(BaseModel):
    id: str
    name: str


class TypeOut(BaseModel):
    id: str
    name: str
