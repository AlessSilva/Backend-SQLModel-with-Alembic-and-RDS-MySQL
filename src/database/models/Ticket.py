from datetime import datetime
from sqlmodel import Field, Relationship, Field
from src.database.models.Base import CustomBase


class Ticket(CustomBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    comentarios: list["Comentario"] = Relationship(back_populates="ticket")
    anexos: list["Anexo"] = Relationship(back_populates="ticket")

    documento: str
    nome_usuario: str
    email_usuario: str
    email_notificacao: str
    titulo: str
    descricao: str
    conta: int
    area: str
    status: str
    data_criacao: datetime = Field(default=datetime.now)
