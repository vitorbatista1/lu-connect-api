from sqlalchemy.orm import Session
from app.models.products import Product
from app.schemas.products import ProductCreate, ProductUpdate
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

def create_product (db: Session, product: ProductCreate):
    db_product = Product(**product.dict())
    db.add(db_product)
    try:
        db.commit()
        db.refresh(db_product)
        return db_product
    except IntegrityError as e:
        if "email" in str(e.orig):
            raise HTTPException(status_code=400, detail="Email already registered")
        if "cpf" in str(e.orig):
            raise HTTPException(status_code=400, detail="CPF already registered")
        
        raise HTTPException(status_code=400, detail="Erro de integridade no banco de dados")


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Product).offset(skip    ).limit(limit).all()

def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


def update_product(db: Session, product_id: int, product_update: ProductUpdate):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        print("Produto não encontrado")
        return None

    print("Antes:", db_product.description, db_product.price_sold)
    for key, value in product_update.dict().items():
        print(f"Atualizando {key} para {value}")
        setattr(db_product, key, value)

    db.commit()
    db.refresh(db_product)
    print("Depois:", db_product.description, db_product.price_sold)
    return db_product



def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    if not db_product:
        return None
    db.delete(db_product)
    db.commit()
    return {
        "message": "O seguinte produto foi deletado",
        "product": db_product
    }