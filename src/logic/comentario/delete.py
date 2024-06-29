from http import HTTPStatus
from sqlmodel import Session, select
from src.database.models.Comentario import Comentario
from src.database.models.Anexo import Anexo
from sqlalchemy.orm import selectinload


def comentario_delete(
    id: int,
    session: Session
):
    print("comentario_delete")

    comentario = session.get(Comentario, id)

    if not comentario:
        raise Exception(f"Comentario com ID {id} não encontrado",
                        HTTPStatus.NOT_FOUND.value)

    for anexo in comentario.anexos:
        session.delete(anexo)

    session.delete(comentario)

    session.commit()

    return HTTPStatus.NO_CONTENT.value, None
