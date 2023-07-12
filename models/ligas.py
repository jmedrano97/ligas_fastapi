from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class Ligas(Base):

    __tablename__ = "ligas"

    id = Column(Integer, primary_key = True)
    nombre = Column(String)
    descripcion = Column(String)