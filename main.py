from fastapi import FastAPI
from routers.ligas import ligas_router
from config.database import engine, Base
# from middlewares.error_handler import ErrorHandler

app = FastAPI()
app.title = "Ligas"
app.version = "0.0.1"
app.include_router(ligas_router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Hello World"}

