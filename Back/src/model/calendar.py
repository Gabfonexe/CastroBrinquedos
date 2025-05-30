
import string
from sqlalchemy import BigInteger, Date
from src.extensions.extensions import db, ma
from dataclasses import dataclass

@dataclass
class Calendar(db.Model):
    __tablename__ = "Calendar"
    id: BigInteger = db.Column(db.BigInteger, primary_key=True)
    date: Date = db.Column(db.Date, nullable=False)
    day_quantity: int = db.Column(db.Integer, default=0) 

@dataclass
class DateUnavailable(db.Model):
    __tablename__ = "Date Unavailable"
    id: BigInteger = db.Column(db.BigInteger, primary_key=True)
    date: Date = db.Column(db.Date, nullable=False)
    reason: string = db.Column(db.String(120),nullable=True) 
    product: string = db.Column(db.String(120),nullable=True) 


