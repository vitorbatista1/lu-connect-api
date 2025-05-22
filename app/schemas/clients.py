from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class ClientBase(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    address: Optional[str] = None
    cpf: Optional[str] = None  
    is_active: bool = True

class ClientCreate(ClientBase):
    pass  

class ClientUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    is_active: Optional[bool] = None

class ClientOut(ClientBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True
