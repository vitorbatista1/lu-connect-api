from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.products import ProductCreate, ProductUpdate, ProductOut
from app.crud.products import get_products, create_product, get_product, delete_product, update_product
from app.db.database import get_db

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/", response_model=List[ProductOut])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    clients = get_products(db, skip=skip, limit=limit)
    return clients

@router.get("/{product_id}", response_model=ProductOut)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = get_product(db, product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Produto nao encontrado")
    return db_product

@router.post("/", response_model=ProductOut)
def create_new_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)

@router.delete("/{product_id}", response_model=ProductOut)
def delete_existing_product(product_id: int, db: Session = Depends(get_db)):
    db_product = delete_product(db, product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Produto nao encontrado")
    return db_product["product"]

@router.put("/{product_id}", response_model=ProductOut)
def update_existing_product(
    product_id: int,
    product_update: ProductUpdate,
    db: Session = Depends(get_db)
):
    db_product = update_product(db, product_id, product_update)
    if not db_product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return db_product