from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4

from workout_api.atleta.AtletaModels import AtletaModel
from workout_api.atleta.schemas import AtletaIn, AtletaOut
from workout_api.contrib.dependencies import DatabaseDependency

from sqlalchemy.future import select



router = APIRouter()

@router.post(
    path='/', 
    summary='Criar novo atleta',
    status_code=status.HTTP_201_CREATED
)
async def post(
    db_session: DatabaseDependency, 
    atleta_in: AtletaIn = Body(...)
) -> AtletaOut: 
    atleta_out = AtletaOut(id=uuid4(), **atleta_in.model_dump())
    atleta_model = AtletaModel(**atleta_out.model_dump())
    
    db_session.add(atleta_model)
    await db_session.commit()

    return atleta_out

@router.get(
    path='/', 
    summary='Consultar todas os atletas',
    status_code=status.HTTP_200_OK,
    response_model=list[AtletaOut],

)
async def query(db_session: DatabaseDependency,  
) -> list[AtletaOut]:
    atletas: list[AtletaOut] = (await db_session.execute(select(AtletaModel))).scalars().all()
    
    return atletas


@router.get(
    path='/{id}', 
    summary='Consultar um atleta por id',
    status_code=status.HTTP_200_OK,
    response_model=AtletaOut,

)
async def query(id: UUID4,db_session: DatabaseDependency,  
) -> AtletaOut:
    atleta: AtletaOut = (
        await db_session.execute(select(AtletaModel).filter_by(id=id))
        ).scalars().first()
    
    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Atleta não encontrado para o id: {id}'
        )
    
    return atleta