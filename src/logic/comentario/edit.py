from http import HTTPStatus
from datetime import datetime
from sqlmodel import Session
from src.database.models.Comentario import Comentario
from src.schemas.InputComentarioEdit import InputComentarioEdit


def comentario_edit(
    id: int,
    body: InputComentarioEdit,
    session: Session
):
    print("comentario_edit")

    body_ = body.model_dump(exclude_defaults=True)
    comentario = session.get(Comentario, id)

    if not comentario:
        raise Exception(f"Comentario com ID {id} não encontrado",
                        HTTPStatus.BAD_REQUEST.value)

    for key, value in body_.items():
        setattr(comentario, key, value)

    session.commit()
    session.refresh(comentario)

    response = {
        'data': comentario.dict()
    }
    return HTTPStatus.OK.value, response
