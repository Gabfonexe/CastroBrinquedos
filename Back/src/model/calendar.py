
import string
from sqlalchemy import BigInteger, Date
from src.extensions.extensions import db, ma
from dataclasses import dataclass

@dataclass
class Calendar(db.Model):
    __tablename__ = "Calendar"
    id: BigInteger = db.Column(db.BigInteger, primary_key=True)
    date: Date = db.Column(db.Date, nullable=False)
    day_quantity: int = db.Column(db.Integer, default=0) #Usar para controlar a quantidade de produtos de aluguel, n pode ser maior que 5


@dataclass
class DateUnavailable(db.Model):
    __tablename__ = "Date Unavailable"
    id: BigInteger = db.Column(db.BigInteger, primary_key=True)
    date: Date = db.Column(db.Date, nullable=False)
    reason: string = db.Column(db.String(120),nullable=True) 


# Se a quantidade de produtos for zerada (is_unavailable), então aquele dia não poderá estar disponível mais. 
# -> talvez criar um tooltip mostrando os produtos disponíveis
# -> se a data não estiver disponível, mostrar o tooltip com o reason;