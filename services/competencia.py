from models.ligas import Competencia as CompetenciaModel


class CompetenciaService():
    
    def __init__(self, db) -> None:
        self.db = db

    def get_competencias(self):
        result = self.db.query(CompetenciaModel).all()
        return result

    def get_competencia_unica(self, id):
        result = self.db.query(CompetenciaModel).filter(CompetenciaModel.id == id).first()
        return result

    # def get_movies_by_category(self, category):
    #     result = self.db.query(CompetenciaModel).filter(CompetenciaModel.category == category).all()
    #     return result

    def create_competencia(self, competencia: CompetenciaModel):
        new_competencia = CompetenciaModel(**competencia.dict())
        self.db.add(new_competencia)
        self.db.commit()
        return

    def update_competencia(self, id: int, data: CompetenciaModel):
        competencia = self.db.query(CompetenciaModel).filter(CompetenciaModel.id == id).first()
        competencia.nombre = data.nombre
        self.db.commit()
        return