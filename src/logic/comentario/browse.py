from sqlmodel import Session, select, func
from sqlalchemy.orm import selectinload
from src.database.models.Comentario import Comentario


def comentario_browse(
    limit: int,
    page: int,
    session: Session
):
    print("comentario_browse")

    query = select(Comentario).options(
        selectinload(Comentario.anexos))

    count_query = select(func.count()).select_from(Comentario)

    total = session.exec(count_query).one()

    query = query.limit(limit).offset((page - 1) * limit)
    results = session.exec(query).all()

    comentario_list = []
    for comentario in results:
        comentario_dict = comentario.dict()
        comentario_dict['anexos'] = [a.dict() for a in comentario.anexos]
        comentario_list.append(comentario_dict)

    response = {
        'data': comentario_list,
        'meta': {
            'limit': limit,
            'page': page,
            'total': total
        }
    }
    return 200, response
