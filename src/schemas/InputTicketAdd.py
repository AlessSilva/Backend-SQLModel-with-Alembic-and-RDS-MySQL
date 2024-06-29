from pydantic import BaseModel, validator
from pydantic_core import PydanticCustomError
from typing import Optional, List
from datetime import datetime


class InputTicketAdd(BaseModel):
    titulo: str
    descricao: str
    conta: int
    email_notificacao: str
    nome_usuario: str
    email_usuario: str
    area: str
    status: str
    data_criacao: str
    documento: str

    # @validator('titulo', always=True, pre=True)
    # def validar_titulo(cls, v, values, **kwargs):
    #     erro = None

    #     if v is None:
    #         erro = 'O campo "titulo" está ausente.'
    #     elif not isinstance(v, str):
    #         erro = f'''O campo "titulo" deve ser do tipo str,
    #         mas o tipo fornecido é {type(v).__name__}.'''
    #     elif v.isspace() or not len(v):
    #         erro = f'''O campo "titulo" deve ser fomado por
    #         caracteres válidos, mas foi fornecido {v}.'''

    #     if erro:
    #         raise PydanticCustomError(
    #             erro,
    #             'value got "{wrong_value}"',
    #             dict(wrong_value=v)
    #         )

    #     return v

    # @validator('descricao', always=True, pre=True)
    # def validar_descricao(cls, v, values, **kwargs):
    #     erro = None

    #     if v is None:
    #         erro = 'O campo "descricao" está ausente.'
    #     elif not isinstance(v, str):
    #         erro = f'''O campo "descricao" deve ser do tipo str,
    #         mas o tipo fornecido é {type(v).__name__}.'''
    #     elif v.isspace() or not len(v):
    #         erro = f'''O campo "descricao" deve ser fomado
    #         por caracteres válidos, mas foi fornecido {v}.'''

    #     if erro:
    #         raise PydanticCustomError(
    #             erro,
    #             'value got "{wrong_value}"',
    #             dict(wrong_value=v)
    #         )

    #     return v

    # @validator('conta', always=True, pre=True)
    # def validar_conta(cls, v, values, **kwargs):
    #     erro = None

    #     if v is None:
    #         erro = 'O campo "conta" está ausente.'
    #     elif not isinstance(v, int):
    #         erro = f'''O campo "conta" deve ser do tipo int,
    #         mas o tipo fornecido é {type(v).__name__}.'''
    #     elif v < 0:
    #         erro = f'''O campo "conta" dever ser
    #         um inteiro positivo, mas foi fornecido {v}.'''

    #     if erro:
    #         raise PydanticCustomError(
    #             erro,
    #             'value got "{wrong_value}"',
    #             dict(wrong_value=v)
    #         )

    #     return v

    # @validator('email_notificacao', always=True, pre=True)
    # def validar_email_notificacao(cls, v, values, **kwargs):
    #     erro = None

    #     if v is None:
    #         erro = 'O campo "email_notificacao" está ausente.'
    #     elif not isinstance(v, str):
    #         erro = f'''O campo "email_notificacao" deve ser do tipo str,
    #         mas o tipo fornecido é {type(v).__name__}.'''
    #     elif v.isspace() or not len(v):
    #         erro = f'''O campo "email_notificacao" deve ser fomado
    #         por caracteres válidos, mas foi fornecido {v}.'''

    #     if erro:
    #         raise PydanticCustomError(
    #             erro,
    #             'value got "{wrong_value}"',
    #             dict(wrong_value=v)
    #         )

    #     return v

    # @validator('email_usuario', always=True, pre=True)
    # def validar_email(cls, v, values, **kwargs):
    #     erro = None

    #     if v is None:
    #         erro = 'O campo "email_usuario" está ausente.'
    #     elif not isinstance(v, str):
    #         erro = f'''O campo "email_usuario" deve ser do tipo str,
    #         mas o tipo fornecido é {type(v).__name__}.'''
    #     elif v.isspace() or not len(v):
    #         erro = f'''O campo "email_usuario" deve ser fomado
    #         por caracteres válidos, mas foi fornecido {v}.'''

    #     if erro:
    #         raise PydanticCustomError(
    #             erro,
    #             'value got "{wrong_value}"',
    #             dict(wrong_value=v)
    #         )

    #     return v

    # @validator('nome_usuario', always=True, pre=True)
    # def validar_nome(cls, v, values, **kwargs):
    #     erro = None

    #     if v is None:
    #         erro = 'O campo "nome_usuario" está ausente.'
    #     elif not isinstance(v, str):
    #         erro = f'''O campo "nome_usuario" deve ser do tipo str,
    #         mas o tipo fornecido é {type(v).__name__}.'''
    #     elif v.isspace() or not len(v):
    #         erro = f'''O campo "nome_usuario" deve ser fomado por
    #         caracteres válidos, mas foi fornecido {v}.'''

    #     if erro:
    #         raise PydanticCustomError(
    #             erro,
    #             'value got "{wrong_value}"',
    #             dict(wrong_value=v)
    #         )

    #     return v

    # @validator('area', always=True, pre=True)
    # def validar_area(cls, v, values, **kwargs):
    #     erro = None

    #     if v is None:
    #         erro = 'O campo "area" está ausente.'
    #     elif not isinstance(v, str):
    #         erro = f'''O campo "area" deve ser do tipo str,
    #         mas o tipo fornecido é {type(v).__name__}.'''
    #     elif v.isspace() or not len(v):
    #         erro = f'''O campo "area" deve ser fomado por
    #         caracteres válidos, mas foi fornecido {v}.'''

    #     if erro:
    #         raise PydanticCustomError(
    #             erro,
    #             'value got "{wrong_value}"',
    #             dict(wrong_value=v)
    #         )

    #     return v

    # @validator('status', always=True, pre=True)
    # def validar_status(cls, v, values, **kwargs):
    #     erro = None

    #     if v is None:
    #         erro = 'O campo "status" está ausente.'
    #     elif not isinstance(v, str):
    #         erro = f'''O campo "status" deve ser do tipo str,
    #         mas o tipo fornecido é {type(v).__name__}.'''
    #     elif v.isspace() or not len(v):
    #         erro = f'''O campo "status" deve ser fomado por
    #         caracteres válidos, mas foi fornecido {v}.'''
    #     elif v not in ['aberto', 'finalizado', 'aguardando',
    #                    'arquivado', 'cancelado']:
    #         l_status = ['aberto', 'finalizado', 'aguardando',
    #                     'arquivado', 'cancelado']
    #         erro = f'''O campo "status" aceita os valores
    #         {l_status}, mas foi fornecido {v}.'''
    #     if erro:
    #         raise PydanticCustomError(
    #             erro,
    #             'value got "{wrong_value}"',
    #             dict(wrong_value=v)
    #         )

    #     return v

    # @validator('data', always=True, pre=True)
    # def validar_data(cls, v, values, **kwargs):
    #     erro = None

    #     if v is None:
    #         erro = 'O campo "data" está ausente.'
    #     elif not isinstance(v, str):
    #         erro = f'''O campo "data" deve ser do tipo str,
    #         mas o tipo fornecido é {type(v).__name__}.'''
    #     else:
    #         try:
    #             datetime.fromisoformat(v)
    #         except ValueError:
    #             erro = '''O campo "data" deve ser fornecido no
    #             formato ISO datetime (aaaa-mm-ddThh:mm:ss).'''

    #     if erro:
    #         raise PydanticCustomError(
    #             erro,
    #             'value got "{wrong_value}"',
    #             dict(wrong_value=v)
    #         )

    #     return v

    # @validator('documento', always=True, pre=True)
    # def validar_documento(cls, v, values, **kwargs):
    #     erro = None

    #     if v is None:
    #         erro = 'O campo "documento" está ausente.'
    #     if not isinstance(v, str):
    #         erro = f'''O campo "documento" deve ser do tipo str,
    #         mas o tipo fornecido é {type(v).__name__}.'''
    #     elif not v.isdigit():
    #         erro = f'''O campo "documento" dever ser formado
    #         apenas por números, mas foi fornecido {v}.'''
    #     elif not int(v) <= 99999999999999:
    #         erro = f'''O campo "documento" deve
    #         ter até 14 dígitos não {len(str(v))}.'''

    #     if erro:
    #         raise PydanticCustomError(
    #             erro,
    #             'value got "{wrong_value}"',
    #             dict(wrong_value=v)
    #         )

    #     return v
