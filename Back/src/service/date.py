
from src.model.date import Dates 
from flask import jsonify
from src.extensions.extensions import db

def add_date(date: Dates):
    exists_date = db.session.query(Dates).filter_by(date=date.date).first()
    if(exists_date):
        exists_date.total_amount += date.total_amount
        db.session.commit()
        return
    
    db.session.add(date)
    db.session.commit()