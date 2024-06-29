from http import HTTPStatus
from sqlmodel import Session
from src.database.models.Ticket import Ticket
from src.database.models.Comentario import Comentario
from src.database.models.Anexo import Anexo
from src.schemas.InputAnexoAdd import InputAnexoAdd
from src.utils.s3 import put_item_s3


def anexo_add(
    body: InputAnexoAdd,
    session: Session,
):
    print("anexo_add")

    if body.ticket_id:
        ticket = session.get(Ticket, body.ticket_id)
        if not ticket:
            raise Exception(f"Ticket com ID {body.ticket_id} não encontrado",
                            HTTPStatus.BAD_REQUEST.value)

    elif body.comentario_id:
        comentario = session.get(Comentario, body.comentario_id)
        if not comentario:
            raise Exception(
                f"Comentario com ID {body.comentario_id} não encontrado",
                HTTPStatus.BAD_REQUEST.value
                )
        ticket_id = comentario.ticket_id

    else:
        raise Exception(f"Informe um id de ticket ou de comentario",
                        HTTPStatus.BAD_REQUEST.value)

    key = put_item_s3(
        file=body.base64_arquivo,
        file_name=body.nome_arquivo,
        content_type=body.tipo_arquivo,
        ticket_id=body.ticket_id,
        comentario_id=body.comentario_id
        )

    data_datetime = datetime.fromisoformat(body.data_upload)
    if comentario_id:
        new_anexo = Anexo(
            key=key,
            nome_arquivo=body.nome_arquivo,
            tipo_arquivo=body.tipo_arquivo,
            comentario_id=body.comentario_id,
            data_upload=data_datetime,
            )

    else:
        new_anexo = Anexo(
            key=key,
            nome_arquivo=body.nome_arquivo,
            tipo_arquivo=body.tipo_arquivo,
            ticket_id=body.ticket_id,
            data_upload=data_datetime,
            )

    session.add(new_anexo)
    session.commit()
    session.refresh(new_anexo)

    response = {
        'data': new_anexo.dict()
    }

    return HTTPStatus.CREATED, response
