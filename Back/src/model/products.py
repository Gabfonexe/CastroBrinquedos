
from sqlalchemy import BigInteger, Integer
from src.extensions.extensions import db, ma
from dataclasses import dataclass
from src.Enum import Types_Products

@dataclass
class Products(db.Model):
    __tablename__ = "Products"
    id: BigInteger = db.Column(db.BigInteger, primary_key=True)
    type: Types_Products = db.Column(db.Enum(Types_Products), nullable=False)
    quantity: Integer = db.Column(db.Integer)
    is_available: bool = db.Column(db.Boolean, default=False)