# from config.database import Base
from config.conexion_mysql import Base
from sqlalchemy import Column, Integer, String, Float,ForeignKey
from sqlalchemy.orm import relationship

class Ligas(Base):

    __tablename__ = "ligas"

    id = Column(Integer, primary_key = True)
    nombre = Column(String(50))
    descripcion = Column(String(100))

    competencia = relationship("Competencia", back_populates="ligas")
    # models.py

class Competencia(Base):
    __tablename__ = "competencias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50))
    ligas_id = Column(Integer, ForeignKey("ligas.id"))

    # Relación con el modelo Author (muchos a uno)
    ligas = relationship("Ligas", back_populates="competencia")
