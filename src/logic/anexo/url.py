import os
from http import HTTPStatus
from sqlmodel import Session
from src.database.models.Anexo import Anexo
from lib.ks2.aws.s3 import create_presigned_url


def anexo_url(
    key: str,
    session: Session,
):
    print("anexo_url")
    anexo = session.get(Anexo, key)

    if not anexo:
        raise Exception(f"Anexo com Key {key} não encontrado",
                        HTTPStatus.BAD_REQUEST.value)

    url = create_presigned_url(bucket_name=os.getenv("BUCKET_NAME"),
                               object_name=anexo.key,
                               expiration=300)

    anexo_dict = {
        'key': anexo.key,
        'url': url,
        'expiration': 300
    }

    response = {
            'data': anexo_dict
            }

    return HTTPStatus.OK.value, response
