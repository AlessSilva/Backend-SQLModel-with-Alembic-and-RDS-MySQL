from http import HTTPStatus
from sqlmodel import Session, select
from src.database.models.Ticket import Ticket
from src.database.models.Comentario import Comentario
from sqlalchemy.orm import selectinload


def ticket_read(
    id: int,
    session: Session
):
    print("ticket_read")

    query = select(Ticket).where(Ticket.id == id).options(
        selectinload(Ticket.comentarios).selectinload(
            Comentario.anexos),
        selectinload(Ticket.anexos))

    ticket = session.exec(query).first()

    if not ticket:
        raise Exception(f"Ticket com ID {id} não encontrado",
                        HTTPStatus.BAD_REQUEST.value)

    ticket_dict = ticket.dict()
    ticket_dict['comentarios'] = []
    for comentario in ticket.comentarios:
        comentario_dict = comentario.dict()
        comentario_dict['anexos'] = [a.dict() for a in comentario.anexos]
        ticket_dict['comentarios'].append(comentario_dict)
    ticket_dict['anexos'] = [a.dict() for a in ticket.anexos]

    response = {
        'data': ticket_dict
    }
    return HTTPStatus.OK.value, response
