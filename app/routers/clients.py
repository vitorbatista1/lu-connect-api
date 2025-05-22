from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.clients import ClientCreate, ClientUpdate, ClientOut
from app.crud.clients import get_client, get_clients, create_client, update_client, delete_client
from app.db.database import get_db

router = APIRouter(prefix="/clients", tags=["clients"])

@router.get("/", response_model=List[ClientOut])
def read_clients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    clients = get_clients(db, skip=skip, limit=limit)
    return clients

@router.get("/{client_id}", response_model=ClientOut)
def read_client(client_id: int, db: Session = Depends(get_db)):
    db_client = get_client(db, client_id)
    if not db_client:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return db_client

@router.post("/", response_model=ClientOut)
def create_new_client(client: ClientCreate, db: Session = Depends(get_db)):
    # Aqui você pode validar se o email/cpf já existe para evitar duplicidade
    return create_client(db, client)

@router.put("/{client_id}", response_model=ClientOut)
def update_existing_client(client_id: int, client_update: ClientUpdate, db: Session = Depends(get_db)):
    db_client = update_client(db, client_id, client_update)
    if not db_client:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return db_client

@router.delete("/{client_id}", response_model=ClientOut)
def delete_existing_client(client_id: int, db: Session = Depends(get_db)):
    db_client = delete_client(db, client_id)
    if not db_client:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return db_client
