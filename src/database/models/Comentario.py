from datetime import datetime
from sqlmodel import Field, Relationship
from src.database.models.Base import CustomBase
from src.database.models.Ticket import Ticket


class Comentario(CustomBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    ticket_id: int | None = Field(default=None, foreign_key="ticket.id")
    ticket: Ticket | None = Relationship(back_populates="comentarios")

    anexos: list["Anexo"] = Relationship(back_populates="comentario")
    texto: str
    email_usuario: str
    nome: str
    data_criacao: datetime = Field(default=datetime.now)
