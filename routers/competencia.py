from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from fastapi.encoders import jsonable_encoder
# from middlewares.jwt_bearer import JWTBearer
from services.competencia import CompetenciaService
from schemas.ligas import Competencia
from models.ligas import Competencia as CompetenciaModel


competencia_router = APIRouter()


@competencia_router.get('/competencias', tags=['competencias'], response_model=List[Competencia], status_code=200)
def get_competencias() -> List[Competencia]:
    db = Session()
    result = CompetenciaService(db).get_competencias()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

# @competencia_router.get('/ligas/{id}', tags=['ligas'], response_model=Ligas)
# def get_ligas(id: int = Path(ge=1, le=2000)) -> Ligas:
#     db = Session()
#     result = LigasService(db).get_liga_unica(id)
#     if not result:
#         return JSONResponse(status_code=404, content={'message': "No encontrado"})
#     return JSONResponse(status_code=200, content=jsonable_encoder(result))

@competencia_router.post('/competencias', tags=['competencias'], response_model=dict, status_code=201)
def create_competencia(competencia: Competencia) -> dict:
    db = Session()
    CompetenciaService(db).create_competencia(competencia)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la competencia"})

# @competencia_router.put('/ligas/{id}', tags=['ligas'], response_model=dict, status_code=200)
# def update_liga(id: int, liga: Ligas)-> dict:
#     db = Session()
#     result = LigasService(db).get_liga_unica(id)
#     if not result:
#         return JSONResponse(status_code=404, content={'message': "No encontrado"})
    
#     LigasService(db).update_liga(id, liga)
#     return JSONResponse(status_code=200, content={"message": "Se ha modificado la Liga"})

# @competencia_router.delete('/ligas/{id}', tags=['ligas'], response_model=dict, status_code=200)
# def delete_liga(id: int)-> dict:
#     db = Session()
#     result = db.query(LigasModel).filter(LigasModel.id == id).first()
#     if not result:
#         return JSONResponse(status_code=404, content={'message': "No encontrado"})
#     db.delete(result)
#     db.commit()
#     return JSONResponse(status_code=200, content={"message": "Se ha eliminado la Liga"})