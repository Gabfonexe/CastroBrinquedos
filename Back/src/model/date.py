from sqlalchemy import BigInteger, Date
from src.extensions.extensions import db, ma
from dataclasses import dataclass


@dataclass
class Dates(db.Model):
    __tablename__ = "Dates"
    id: BigInteger = db.Column(db.BigInteger,primary_key=True)
    date: Date = db.Column(db.Date, nullable=False)
    total_amount: float = db.Column(db.Float)