from sqlalchemy import Column, Integer, String
from app.db.database import Base


class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    price_sold = Column(String, nullable=False)
    cod_bar = Column(String, nullable=False)
    session = Column(String, nullable=False)
    stock_quantity = Column(String, nullable=False)
    date_validity = Column(String, nullable=True)
    image = Column(String, nullable=False)

    def __repr__(self):
        return f"Product(id={self.id}, description={self.description}, price_sold={self.price_sold})"
    
    