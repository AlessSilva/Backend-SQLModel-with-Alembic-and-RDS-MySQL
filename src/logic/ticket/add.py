from datetime import datetime
from sqlmodel import Session
from src.database.models.Ticket import Ticket
from src.schemas.InputTicketAdd import InputTicketAdd


def ticket_add(
    body: InputTicketAdd,
    session: Session
):
    print("ticket_add")

    data_datetime = datetime.fromisoformat(body.data_criacao)
    new_ticket = Ticket(
        documento=body.documento,
        nome_usuario=body.nome_usuario,
        email_usuario=body.email_usuario,
        email_notificacao=body.email_notificacao,
        titulo=body.titulo,
        descricao=body.descricao,
        conta=body.conta,
        area=body.area,
        status=body.status,
        data_criacao=data_datetime,
    )

    session.add(new_ticket)
    session.commit()
    session.refresh(new_ticket)

    response = {
        'data': new_ticket.dict()
    }
    return 201, response
