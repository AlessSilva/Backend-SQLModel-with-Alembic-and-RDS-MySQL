from typing import Optional
from http import HTTPStatus

from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.event_handler.openapi.params import Query
from aws_lambda_powertools.shared.types import Annotated

from src.database.connection import get_session

from src.logic.create import schema_create

from src.logic.ticket.add import ticket_add
from src.logic.ticket.browse import ticket_browse
from src.logic.ticket.edit import ticket_edit
from src.logic.ticket.read import ticket_read
from src.logic.ticket.delete import ticket_delete


from src.logic.comentario.add import comentario_add
from src.logic.comentario.browse import comentario_browse
from src.logic.comentario.edit import comentario_edit
from src.logic.comentario.read import comentario_read
from src.logic.comentario.delete import comentario_delete

from src.logic.anexo.add import anexo_add
from src.logic.anexo.browse import anexo_browse
from src.logic.anexo.read import anexo_read
from src.logic.anexo.url import anexo_url

from src.schemas.InputTicketAdd import InputTicketAdd
from src.schemas.InputTicketEdit import InputTicketEdit

from src.schemas.InputComentarioAdd import InputComentarioAdd
from src.schemas.InputComentarioEdit import InputComentarioEdit

from src.schemas.InputAnexoAdd import InputAnexoAdd

from src.utils.event import handle_exception

app = APIGatewayRestResolver(enable_validation=True)


@app.get("/ping")
def ping() -> dict:
    return {'message': 'ok'}, HTTPStatus.OK


@app.post("/create")
def api_schema_create():
    try:
        session = get_session()
        status, response = schema_create(session)
    except Exception as e:
        status, response = handle_exception(e)

    return response, status


@app.get("/ticket/browse")
def api_ticket_browse(
    inicio: Annotated[Optional[str], Query()] = None,
    fim: Annotated[Optional[str], Query()] = None,
    status: Annotated[Optional[str], Query()] = None,
    assunto: Annotated[Optional[str], Query()] = None,
    documento: Annotated[Optional[str], Query()] = None,
    id: Annotated[Optional[int], Query()] = None,
    limit: Annotated[Optional[int], Query()] = 6,
    page: Annotated[Optional[int], Query()] = 1,
):
    try:
        session = get_session()
        status, response = ticket_browse(inicio, fim, status, assunto,
                                         documento, id, limit, page,
                                         session)
    except Exception as e:
        status, response = handle_exception(e)

    return response, status


@app.get("/ticket/read")
def api_ticket_read(
    id: Annotated[int, Query()],
):
    try:
        session = get_session()
        status, response = ticket_read(id,
                                       session)
    except Exception as e:
        status, response = handle_exception(e)

    return response, status


@app.put("/ticket/edit")
def api_ticket_edit(
    body: InputTicketEdit,
    id: Annotated[int, Query()]
):
    try:
        session = get_session()
        status, response = ticket_edit(id, body,
                                       session)
    except Exception as e:
        status, response = handle_exception(e)

    return response, status


@app.post("/ticket/add")
def api_ticket_add(
    body: InputTicketAdd
):

    try:
        session = get_session()
        status, response = ticket_add(body, session)
    except Exception as e:
        status, response = handle_exception(e)

    return response, status


@app.delete("/ticket/delete")
def api_ticket_delete(
    id: Annotated[int, Query()]
):
    try:
        session = get_session()
        status, response = ticket_delete(id,
                                         session)
    except Exception as e:
        status, response = handle_exception(e)

    return response, status


@app.get("/comentario/browse")
def api_comentario_browse(
    limit: Annotated[Optional[int], Query()] = 30,
    page: Annotated[Optional[int], Query()] = 1,
):
    try:
        session = get_session()
        status, response = comentario_browse(limit, page,
                                             session)
    except Exception as e:
        status, response = handle_exception(e)

    return response, status


@app.get("/comentario/read")
def api_comentario_read(
    id: Annotated[int, Query()],
):
    try:
        session = get_session()
        status, response = comentario_read(id,
                                           session)
    except Exception as e:
        status, response = handle_exception(e)

    return response, status


@app.put("/comentario/edit")
def api_comentario_edit(
    body: InputComentarioEdit,
    id: Annotated[int, Query()]
):
    try:
        session = get_session()
        status, response = comentario_edit(id, body,
                                           session)
    except Exception as e:
        status, response = handle_exception(e)

    return response, status


@app.post("/comentario/add")
def api_comentario_add(
    body: InputComentarioAdd
):

    try:
        session = get_session()
        status, response = comentario_add(body, session)
    except Exception as e:
        status, response = handle_exception(e)

    return response, status


@app.delete("/comentario/delete")
def api_comentario_delete(
    id: Annotated[int, Query()]
):
    try:
        session = get_session()
        status, response = comentario_delete(id,
                                             session)
    except Exception as e:
        status, response = handle_exception(e)

    return response, status


@app.get("/anexo/browse")
def api_anexo_browse(
    limit: Annotated[Optional[int], Query()] = 30,
    page: Annotated[Optional[int], Query()] = 1,
):
    try:
        session = get_session()
        status, response = anexo_browse(limit, page,
                                        session)
    except Exception as e:
        status, response = handle_exception(e)

    return response, status


@app.post("/anexo/add")
def api_ticket_add(
    body: InputAnexoAdd
):

    try:
        session = get_session()
        status, response = anexo_add(body, session)
    except Exception as e:
        status, response = handle_exception(e)

    return response, status


@app.get("/anexo/read")
def api_anexo_read(
    key: Annotated[str, Query()],
):
    try:
        session = get_session()
        status, response = anexo_read(key,
                                      session)
    except Exception as e:
        status, response = handle_exception(e)

    return response, status


@app.get("/anexo/url")
def api_anexo_url(
    key: Annotated[str, Query()],
):
    try:
        session = get_session()
        status, response = anexo_url(key,
                                     session)
    except Exception as e:
        status, response = handle_exception(e)

    return response, status


def lambda_handler(event: dict, context: LambdaContext) -> dict:
    return app.resolve(event, context)
