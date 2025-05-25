from pydantic import BaseModel, EmailStr


class ProductCreate(BaseModel):
    description: str
    price_sold: str
    cod_bar: str
    session: int
    stock_quantity: int
    date_validity: str
    image: str

class ProductOut(BaseModel):
    id: int
    description: str
    price_sold: str 
    cod_bar: str
    session: str
    stock_quantity: str
    date_validity: str | None
    image: str

    class Config:
      from_attributes = True

class ProductUpdate(BaseModel):
    description: str
    price_sold: str
