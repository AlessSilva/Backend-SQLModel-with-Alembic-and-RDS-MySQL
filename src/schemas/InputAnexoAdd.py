from pydantic import BaseModel, validator
from pydantic_core import PydanticCustomError
from typing import Optional, List
from datetime import datetime


class InputAnexoAdd(BaseModel):
    tipo_arquivo: str
    nome_arquivo: str
    base64_arquivo: str
    ticket_id: Optional[int] = None
    comentario_id: Optional[int] = None
    data_upload: str
