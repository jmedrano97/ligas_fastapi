from pydantic import BaseModel, Field
from typing import Optional, List


class Ligas(BaseModel):
    id: Optional[int] = None
    nombre: str = Field(min_length=5, max_length=15)
    descripcion: str = Field(min_length=15, max_length=50)

    class Config:
        schema_extra = {
            "example": {
                "nombre": "Liga amateur 1",
                "descripcion": "Liga que se jugara en ...",
            }
        }


class Competencia(BaseModel):
    id: Optional[int] = None
    nombre: str = Field(min_length=1, max_length=15)
    Ligas_id: int

    class Config:
        schema_extra = {
            "example": {
                "nombre": "Copa",
                "descripcion": "Eliminación directa",
                "Ligas_id": "1",
            }
        }