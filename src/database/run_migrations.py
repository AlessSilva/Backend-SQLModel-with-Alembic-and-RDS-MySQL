import os
import sys
from alembic import command
from alembic.config import Config
from dotenv import load_dotenv


load_dotenv()

username = os.getenv('MYSQL_DB_USERNAME')
password = os.getenv('MYSQL_DB_PASSWORD')
host = os.getenv('MYSQL_DB_HOST')
port = os.getenv('MYSQL_DB_PORT')
database = os.environ['MYSQL_DB_NAME']
driver = "mysql+mysqlconnector"

url = f"{driver}://{username}:{password}@{host}/{database}"


def run_alembic(
    message: str
):
    current_dir = os.path.dirname(os.path.abspath(__file__))

    alembic_ini_path = os.path.join(current_dir,
                                    'alembic.ini')

    alembic_dir_path = os.path.join(current_dir,
                                    'alembic')

    alembic_cfg = Config(alembic_ini_path)

    alembic_cfg.set_main_option("sqlalchemy.url", url)
    alembic_cfg.set_main_option("script_location", alembic_dir_path)

    command.revision(alembic_cfg,
                     autogenerate=True,
                     message=message)

    command.upgrade(alembic_cfg, "head")

    print("Migrações do Alembic aplicadas com sucesso.")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        message = sys.argv[1]
    else:
        message = "Atualização automática das tabelas"
    run_alembic(message)
