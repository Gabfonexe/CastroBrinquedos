
from sqlalchemy import BigInteger, Date
from src.extensions.extensions import db, ma
from dataclasses import dataclass

@dataclass
class Calendar(db.Model):
    __tablename__ = "Calendar"
    id: BigInteger = db.Column(db.BigInteger, primary_key=True)
    date: Date = db.Column(db.Date, nullable=False)
    day_quantity: int = db.Column(db.Integer, default=0) #Usar para controlar a quantidade de produtos de aluguel, n pode ser maior que 5


