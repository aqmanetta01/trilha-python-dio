from datetime import datetime
from pydantic import UUID4, Field, PositiveFloat
from typing import Annotated

from sqlalchemy import DateTime

from workout_api.contrib.schemas import BaseSchema, OutMixin

class AtletaIn(BaseSchema):
    nome: Annotated[str, Field(description= 'Nome do atleta', example='Joao', max_length=50)]
    cpf: Annotated[str, Field(description= 'CPF do atleta', example='12345678910', max_length=11)]
    idade: Annotated[int, Field(description= 'Idade do atleta', example=25)]
    peso: Annotated[PositiveFloat, Field(description= 'Peso do atleta', example=75.5)]
    altura: Annotated[PositiveFloat, Field(description= 'Altura do atleta', example=1.80)]
    sexo: Annotated[str, Field(description= 'Sexo do atleta', example='M', max_length=1)]
    created_at: Annotated[datetime, Field(description= 'Data da criação do atleta', default=datetime.now())]
    categoria_id: Annotated[int, Field(description='Identificador da categoria do atleta', example=1)]
    centro_treinamento_id: Annotated[int,Field(description='Identificador do centro de treinamento do atleta', example=1)]


class AtletaOut(AtletaIn, OutMixin):
    id: Annotated[UUID4, Field(description='Identificador do atleta')]
