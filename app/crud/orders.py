from sqlalchemy.orm import Session
from app.models.products import Product
from app.schemas.orders import *
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

def create_order(db: Session, order: OrderCreate):
    db_order = Order(**order.dict())
    db.add(db_order)
    try:
        db.commit()
        db.refresh(db_order)
        return db_order
    except IntegrityError as e:
        if "email" in str(e.orig):
            raise HTTPException(status_code=400, detail="Email already registered")
        if "cpf" in str(e.orig):
            raise HTTPException(status_code=400, detail="CPF already registered")
        
        raise HTTPException(status_code=400, detail="Erro de integridade no banco de dados")
    
