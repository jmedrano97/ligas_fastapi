from config.database import Base
from sqlalchemy import Column, Integer, String, Float,ForeignKey
from sqlalchemy.orm import relationship

class Ligas(Base):

    __tablename__ = "ligas"

    id = Column(Integer, primary_key = True)
    nombre = Column(String)
    descripcion = Column(String)

    competencia = relationship("Competencia", back_populates="ligas")
    # models.py

class Competencia(Base):
    __tablename__ = "competencias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    Ligas_id = Column(Integer, ForeignKey("ligas.id"))

    # Relación con el modelo Author (muchos a uno)
    ligas = relationship("Ligas", back_populates="competencia")
