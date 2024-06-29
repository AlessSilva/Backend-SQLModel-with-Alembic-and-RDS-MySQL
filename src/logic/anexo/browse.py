from sqlmodel import Session, select, func
from src.database.models.Anexo import Anexo


def anexo_browse(
    limit: int,
    page: int,
    session: Session
):
    print("anexo_browse")

    query = select(Anexo)

    count_query = select(func.count()).select_from(Anexo)

    total = session.exec(count_query).one()

    query = query.limit(limit).offset((page - 1) * limit)
    results = session.exec(query).all()

    anexo_list = [anexo.dict() for anexo in results]

    response = {
        'data': anexo_list,
        'meta': {
            'limit': limit,
            'page': page,
            'total': total
        }
    }
    return 200, response
