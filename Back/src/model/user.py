
from sqlalchemy import BigInteger
from src.extensions.extensions import db, ma
from dataclasses import dataclass


@dataclass
class Users(db.Model):
    __tablename__ = "users"
    id: BigInteger = db.Column(db.BigInteger, primary_key=True)
    name: str = db.Column(db.String(250))
    email: str = db.Column(db.String(200))
    number: str = db.Column(db.String(30))
    message: str = db.Column(db.String(700))
    date: str = db.Column(db.String(100))
    budget: float = db.Column(db.Float)
    is_confirmed: bool = db.Column(db.Boolean, default=False)
