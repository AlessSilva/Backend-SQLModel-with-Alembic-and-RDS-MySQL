import os
from src.database.models.Ticket import Ticket
from src.database.models.Comentario import Comentario
from src.database.models.Anexo import Anexo
from src.database.connection import create_tables, list_tables
from sqlmodel import Session


def schema_create(
    session: Session
):
    print('schema_create')
    db_name = os.getenv('MYSQL_DB_NAME')
    try:
        create_tables(tables=[Ticket, Comentario, Anexo],
                      session=session)
        list_tables(session)
        response = {
            'message': f'Schema criado ou atualizado no database {db_name}'
        }
        return 200, response
    except Exception as e:
        raise Exception(500, f'Database {db_name}: {e}')
