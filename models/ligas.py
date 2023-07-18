# from config.database import Base
from config.conexion_mysql import Base
from sqlalchemy import Column, Integer, String, Float

class Ligas(Base):

    __tablename__ = "ligas"

    id = Column(Integer, primary_key = True)
    nombre = Column(String(50))
    descripcion = Column(String(100))