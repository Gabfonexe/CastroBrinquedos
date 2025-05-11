
from src.model.date import Dates 
from flask import jsonify
from src.extensions.extensions import db

def add_date(new_date: Dates):
    try:
        exists_date = db.session.query(Dates).filter(Dates.date==new_date.date).first()
        if(exists_date):
            exists_date.total_amount += new_date.total_amount
            db.session.commit()
            return
        
        db.session.add(new_date)
        db.session.commit()

    except Exception as e:
        print('Error: ', e)