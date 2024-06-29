from datetime import datetime
from sqlmodel import Session
from src.database.models.Comentario import Comentario
from src.schemas.InputComentarioAdd import InputComentarioAdd


def comentario_add(
    body: InputComentarioAdd,
    session: Session
):
    print("comentario_add")

    data_datetime = datetime.fromisoformat(body.data_criacao)
    new_comentario = Comentario(
        ticket_id=body.ticket_id,
        texto=body.texto,
        email_usuario=body.email_usuario,
        nome=body.nome,
        data_cricao=data_datetime,
    )

    session.add(new_comentario)
    session.commit()
    session.refresh(new_comentario)

    response = {
        'data': new_comentario.dict()
    }

    return 201, response
