from http import HTTPStatus
from sqlmodel import Session, select
from src.database.models.Comentario import Comentario
from sqlalchemy.orm import selectinload


def comentario_read(
    id: int,
    session: Session
):
    print("coementario_read")

    query = select(Comentario).where(Comentario.id == id).options(
        selectinload(Comentario.anexos))

    comentario = session.exec(query).first()

    if not comentario:
        raise Exception(f"Comentario com ID {id} não encontrado",
                        HTTPStatus.BAD_REQUEST.value)

    comentario_dict = comentario.dict()
    comentario_dict['anexos'] = [a.dict() for a in comentario.anexos]

    response = {
        'data': comentario_dict
    }
    return HTTPStatus.OK.value, response
