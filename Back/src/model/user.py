
from typing import List
from sqlalchemy import BigInteger, Date
from src.extensions.extensions import db, ma
from dataclasses import dataclass
from sqlalchemy.orm import Mapped, mapped_column, relationship



@dataclass
class Users(db.Model):
    __tablename__ = "users"
    id: BigInteger = db.Column(db.BigInteger, primary_key=True)
    name: str = db.Column(db.String(250))
    email: str = db.Column(db.String(200))
    number: str = db.Column(db.String(30))
    message: str = db.Column(db.String(700))
    date: Date = db.Column(db.Date, nullable=False)
    budget: float = db.Column(db.Float)
    is_confirmed: bool = db.Column(db.Boolean, default=False)
    is_checked: bool =  db.Column(db.Boolean, default=False)
    is_dayli_confirmed: bool = db.Column(db.Boolean, default=False)
    # products: Mapped[list["Products"]] = relationship('Products', secondary='user_products', backref='users')
    products: List[dict] = db.Column(db.JSON)

user_products = db.Table(
    'user_products',
    db.Column('user_id', db.BigInteger, db.ForeignKey('users.id'), primary_key=True),
    db.Column('product_id', db.BigInteger, db.ForeignKey('Products.id'), primary_key=True)
)
