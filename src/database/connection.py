import os
from typing import List
from sqlalchemy import URL
from sqlalchemy.orm import sessionmaker
from sqlmodel import (create_engine,
                      Session,
                      text,
                      inspect,
                      SQLModel)


url_object = URL.create(
    "mysql+mysqlconnector",
    username=os.getenv('MYSQL_DB_USERNAME'),
    password=os.getenv('MYSQL_DB_PASSWORD'),
    host=os.getenv('MYSQL_DB_HOST'),
    port=int(os.getenv('MYSQL_DB_PORT')),
    database=os.environ['MYSQL_DB_NAME']
)

engine = create_engine(url_object)
SessionMaker = sessionmaker(bind=engine, class_=Session)
current_session = None


def get_session(
):
    global current_session
    print("get_session")
    if current_session is None or not current_session.is_active:
        current_session = SessionMaker()
        print("Nova sessão criada.")
    else:
        print("Sessão existente reutilizada.")
    return current_session


def close_session(
    session: Session
):
    print("close_session")
    session.close()


def check_database_connection(
    session: Session
):
    print("check_database_connection")
    try:
        session.exec(text("SELECT 1"))
        print("Conexão com o banco de dados estabelecida com sucesso!")
        return True
    except Exception as e:
        raise Exception(f"Erro ao conectar ao banco de dados ({e})")


def list_databases(
    session: Session
):
    print("list_databases")
    inspector = inspect(session.bind)
    databases = inspector.get_schema_names()
    print("Bancos de dados disponíveis:")
    for db in databases:
        print(db)


def list_tables(
    session: Session
):
    print("list_tables")
    inspector = inspect(session.bind)
    tables = inspector.get_table_names()
    print("Tabelas disponíveis no banco de dados:")
    for table in tables:
        print(table)


def create_tables(
    tables: List[SQLModel],
    session: Session
):
    print("create_tables")
    for i, table in enumerate(tables):
        tables[i] = table.__table__
    if check_database_connection(session):
        try:
            SQLModel.metadata.create_all(bind=engine,
                                         tables=tables)
            print("Tabelas criadas/atualizadas no banco de dados.")

        except Exception as e:
            raise Exception(f"Erro ao criar/atualizar tabelas ({e})")
