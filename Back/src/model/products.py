
import string
from sqlalchemy import BigInteger, Integer
from src.extensions.extensions import db, ma
from dataclasses import dataclass
from src.Enum import Types_Products


@dataclass
class Products(db.Model):
    __tablename__ = "Products"

    id: BigInteger = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    type: Types_Products = db.Column(db.Enum(Types_Products), nullable=False, unique=True)
    description: string = db.Column(db.String(180))
    quantity: Integer = db.Column(db.Integer)
    is_available: bool = db.Column(db.Boolean, default=False)
    price: float = db.Column(db.Float)
    image: string = db.Column(db.String(250)) 
    lost_quantity: int = db.Column(db.Integer, default=0)
    static_quantity: Integer = db.Column(db.Integer)


