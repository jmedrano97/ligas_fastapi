from models.ligas import Ligas as LigasModel


class LigasService():
    
    def __init__(self, db) -> None:
        self.db = db

    def get_ligas(self):
        result = self.db.query(LigasModel).all()
        return result

    def get_liga_unica(self, id):
        result = self.db.query(LigasModel).filter(LigasModel.id == id).first()
        return result

    # def get_movies_by_category(self, category):
    #     result = self.db.query(LigasModel).filter(LigasModel.category == category).all()
    #     return result

    def create_liga(self, ligas: LigasModel):
        new_liga = LigasModel(**ligas.dict())
        self.db.add(new_liga)
        self.db.commit()
        return

    def update_liga(self, id: int, data: LigasModel):
        liga = self.db.query(LigasModel).filter(LigasModel.id == id).first()
        liga.nombre = data.nombre
        liga.descripcion = data.descripcion
        self.db.commit()
        return