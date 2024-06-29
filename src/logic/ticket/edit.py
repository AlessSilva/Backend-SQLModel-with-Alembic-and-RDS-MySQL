from http import HTTPStatus
from datetime import datetime
from sqlmodel import Session
from src.database.models.Ticket import Ticket
from src.schemas.InputTicketEdit import InputTicketEdit


def ticket_edit(
    id: int,
    body: InputTicketEdit,
    session: Session
):
    print("ticket_edit")

    body_ = body.model_dump(exclude_defaults=True)
    ticket = session.get(Ticket, id)

    if not ticket:
        raise Exception(f"Ticket com ID {id} não encontrado",
                        HTTPStatus.BAD_REQUEST.value)

    for key, value in body_.items():
        setattr(ticket, key, value)

    session.commit()
    session.refresh(ticket)

    response = {
        'data': ticket.dict()
    }
    return HTTPStatus.OK.value, response
