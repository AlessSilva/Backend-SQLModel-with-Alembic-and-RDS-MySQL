from datetime import datetime
from sqlmodel import Field, Relationship
from src.database.models.Base import CustomBase
from src.database.models.Ticket import Ticket
from src.database.models.Comentario import Comentario


class Anexo(CustomBase, table=True):
    key: str | None = Field(default=None, primary_key=True)

    ticket_id: int | None = Field(default=None, foreign_key="ticket.id")
    ticket: Ticket | None = Relationship(back_populates="anexos")

    comentario_id: int | None = Field(
        default=None, foreign_key="comentario.id"
        )
    comentario: Comentario | None = Relationship(back_populates="anexos")

    nome_arquivo: str
    tipo_arquivo: str
    data_upload: datetime = Field(default=datetime.now)
