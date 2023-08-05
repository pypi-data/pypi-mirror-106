from enum import Enum
from typing import Optional

from pydantic import BaseModel, confloat

XML_TEMPLATE = """
<video>
<id>{ID}</id>
<filename>{FILENAME}</filename>
<data>{DATETIME}</data>
<retranca>{RETRANCA}</retranca>
<descricao>{DESCRIPTION}</descricao>
<card>{CARD}</card>
<destino>{WORKSPACE}</destino>
<usuario>{USER}</usuario>
</video>
"""


class MediaStatus(Enum):
    pending = "pending"
    processing = "processing"
    success = "success"
    rename = "rename"
    error = "error"


class Media(BaseModel):
    name: str
    path: str
    mimetype: str
    size: int
    sent: int = 0
    complete_percentage: confloat(ge=0.0, le=100.0) = 0.0
    status: MediaStatus = MediaStatus.pending

    def dict(self, *args, **kargs):
        _dict = super().dict(*args, **kargs)
        _dict["status"] = self.status.value
        return _dict


class XmlData(BaseModel):
    id: str
    filename: str
    datetime: str
    retranca: str
    description: Optional[str] = ""
    card: str
    workspace: str
    username: str
    status: MediaStatus = MediaStatus.pending

    def get_xml_str(self):
        xml = XML_TEMPLATE.format(
            FILENAME=self.filename,
            DESCRIPTION=self.description,
            ID=self.id,
            DATETIME=self.datetime,
            CARD=self.card,
            RETRANCA=self.retranca,
            WORKSPACE=self.workspace,
            USER=self.username,
        )
        xml_buffer = xml.encode()
        return xml_buffer

    def dict(self, *args, **kargs):
        _dict = super().dict(*args, **kargs)
        _dict["status"] = self.status.value
        return _dict


class MediaContainer(BaseModel):
    id: str
    media: Media
    xml: XmlData
