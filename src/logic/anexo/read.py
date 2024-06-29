import os
from http import HTTPStatus
from sqlmodel import Session
from src.database.models.Anexo import Anexo


def anexo_read(
    key: str,
    session: Session,
):
    print("anexo_read")
    anexo = session.get(Anexo, key)

    if not anexo:
        raise Exception(f"Anexo com Key {key} não encontrado",
                        HTTPStatus.BAD_REQUEST.value)

    response = {
            'data': anexo.dict()
            }

    return HTTPStatus.OK.value, response
