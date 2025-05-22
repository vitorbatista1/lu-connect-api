from sqlalchemy.orm import Session
from app.models.clients import Client
from app.schemas.clients import ClientCreate, ClientUpdate
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException



def get_client(db: Session, client_id: int):
    return db.query(Client).filter(Client.id == client_id).first()

def get_clients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Client).offset(skip).limit(limit).all()

def create_client(db: Session, client: ClientCreate):
    db_client = Client(**client.dict())
    db.add(db_client)
    try:
        db.commit()
        db.refresh(db_client)
        return db_client
    except IntegrityError as e:
        if "email" in str(e.orig):
            raise HTTPException(status_code=400, detail="Email already registered")
        if "cpf" in str(e.orig):
            raise HTTPException(status_code=400, detail="CPF already registered")
        
        raise HTTPException(status_code=400, detail="Erro de integridade no banco de dados")
        
        

def update_client(db: Session, client_id: int, client_update: ClientUpdate):
    db_client = get_client(db, client_id)
    if not db_client:
        return None
    update_data = client_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_client, key, value)
    db.commit()
    db.refresh(db_client)
    return db_client

def delete_client(db: Session, client_id: int):
    db_client = get_client(db, client_id)
    if not db_client:
        return None
    db.delete(db_client)
    db.commit()
    return db_client
