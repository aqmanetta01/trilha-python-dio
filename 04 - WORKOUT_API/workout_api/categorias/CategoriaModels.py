#from workout_api.atleta.AtletaModels import AtletaModel
from workout_api.contrib.models import BaseModel
from sqlalchemy import  Integer, String
from sqlalchemy.orm import mapped_column, Mapped, relationship

class CategoriaModel(BaseModel):
    __tablename__ = 'categorias'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50),unique=True, nullable=False)
    atleta: Mapped['AtletaModel'] = relationship('AtletaModel',back_populates='categoria') # type: ignore

    