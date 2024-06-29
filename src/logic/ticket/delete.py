from http import HTTPStatus
from sqlmodel import Session
from src.database.models.Ticket import Ticket


def ticket_delete(
    id: int,
    session: Session
):
    print("ticket_delete")

    ticket = session.get(Ticket, id)

    if not ticket:
        raise Exception(f"Ticket com ID {id} não encontrado",
                        HTTPStatus.NOT_FOUND.value)

    for comentario in ticket.comentarios:
        for anexo in comentario.anexos:
            session.delete(anexo)
        session.delete(comentario)

    for anexo in ticket.anexos:
        session.delete(anexo)

    session.delete(ticket)

    session.commit()

    return HTTPStatus.NO_CONTENT.value, None
