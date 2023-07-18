from fastapi import FastAPI
from routers.ligas import ligas_router
from config.conexion_mysql import engine, Base
# from config.database import engine, Base
from routers.competencia import competencia_router
# from middlewares.error_handler import ErrorHandler

app = FastAPI()
app.title = "Ligas"
app.version = "0.0.1"
app.include_router(ligas_router)
app.include_router(competencia_router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Hello World"}

