from fastapi import FastAPI
from app.routers import auth, clients
from app.db.database import create_db_and_tables

app = FastAPI(title="Lu Estilo API", version="1.0.0")

@app.on_event("startup")
def startup():
    create_db_and_tables()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(clients.router)
