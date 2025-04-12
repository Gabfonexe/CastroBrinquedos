
from sqlalchemy import BigInteger, Integer, String
from extensions.extensions import db, ma
from dataclasses import dataclass
from src.Enum import Types_Products

@dataclass
class Products(db.Model):
    id: BigInteger = db.Column(db.BigInteger, primary_key=True)
    type: Types_Products = db.Column(db.SqlEnum(Types_Products), nullable=False)
    quantity: Integer = db.Column(db.Integer)
    