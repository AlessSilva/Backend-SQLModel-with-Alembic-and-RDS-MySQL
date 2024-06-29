from sqlmodel import Session, select, func
from sqlalchemy.orm import selectinload
from src.database.models.Ticket import Ticket
from src.database.models.Comentario import Comentario


def ticket_browse(
    inicio: str | None,
    fim: str | None,
    status: str | None,
    assunto: str | None,
    documento: str | None,
    id: int | None,
    limit: int,
    page: int,
    session: Session
):
    print("ticket_browse")

    query = select(Ticket).options(
        selectinload(Ticket.comentarios).selectinload(
            Comentario.anexos),
        selectinload(Ticket.anexos))

    count_query = select(func.count()).select_from(Ticket)

    if inicio:
        query = query.where(Ticket.data_criacao >= inicio)

        count_query = count_query.where(Ticket.data_criacao >= inicio)

    if fim:
        query = query.where(Ticket.data_criacao <= fim)

        count_query = count_query.where(Ticket.data_criacao <= fim)
    if status:
        query = query.where(Ticket.status == status)

        count_query = count_query.where(Ticket.status == status)
    if assunto:
        query = query.where(
            (Ticket.titulo.ilike(f"%{assunto}%")) |
            (Ticket.descricao.ilike(f"%{assunto}%"))
        )

        count_query = count_query.where(
            (Ticket.titulo.ilike(f"%{assunto}%")) |
            (Ticket.descricao.ilike(f"%{assunto}%"))
        )
    if documento:
        query = query.where(Ticket.documento == documento)

        count_query = count_query.where(Ticket.documento == documento)
    if id:
        query = query.where(Ticket.id == id)

        count_query = count_query.where(Ticket.id == id)

    total = session.exec(count_query).one()

    query = query.limit(limit).offset((page - 1) * limit)
    results = session.exec(query).all()

    tickets_list = []
    for ticket in results:
        ticket_dict = ticket.dict()
        ticket_dict['comentarios'] = []
        for comentario in ticket.comentarios:
            comentario_dict = comentario.dict()
            comentario_dict['anexos'] = [a.dict() for a in comentario.anexos]
            ticket_dict['comentarios'].append(comentario_dict)
        ticket_dict['anexos'] = [a.dict() for a in ticket.anexos]
        tickets_list.append(ticket_dict)

    response = {
        'data': tickets_list,
        'meta': {
            'limit': limit,
            'page': page,
            'total': total
        }
    }
    return 200, response
