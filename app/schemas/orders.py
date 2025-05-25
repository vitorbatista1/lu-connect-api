from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class OrderBase(BaseModel):
    client_id: int    
    product_id: int
    quantity: int

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class OrderUpdate(BaseModel):
    client_id: Optional[int] = None
    product_id: Optional[int] = None
    quantity: Optional[int] = None

    class Config:
        orm_mode = True

class OrderOut(BaseModel):
    id: int
    client_id: int
    product_id: int
    quantity: int
    created_at: datetime

    class Config:
        orm_mode = True