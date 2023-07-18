from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from typing import List
# from config.database import Session
from config.conexion_mysql import Session
from fastapi.encoders import jsonable_encoder
# from middlewares.jwt_bearer import JWTBearer
from services.ligas import LigasService
from schemas.ligas import Ligas
from models.ligas import Ligas as LigasModel

ligas_router = APIRouter()


@ligas_router.get('/ligas', tags=['ligas'], response_model=List[Ligas], status_code=200)
def get_ligas() -> List[Ligas]:
    db = Session()
    result = LigasService(db).get_ligas()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@ligas_router.get('/ligas/{id}', tags=['ligas'], response_model=Ligas)
def get_ligas(id: int = Path(ge=1, le=2000)) -> Ligas:
    db = Session()
    result = LigasService(db).get_liga_unica(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@ligas_router.post('/ligas', tags=['ligas'], response_model=dict, status_code=201)
def create_liga(ligas: Ligas) -> dict:
    db = Session()
    LigasService(db).create_liga(ligas)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la Liga"})

@ligas_router.put('/ligas/{id}', tags=['ligas'], response_model=dict, status_code=200)
def update_liga(id: int, liga: Ligas)-> dict:
    db = Session()
    result = LigasService(db).get_liga_unica(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    
    LigasService(db).update_liga(id, liga)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado la Liga"})

@ligas_router.delete('/ligas/{id}', tags=['ligas'], response_model=dict, status_code=200)
def delete_liga(id: int)-> dict:
    db = Session()
    result = db.query(LigasModel).filter(LigasModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado la Liga"})