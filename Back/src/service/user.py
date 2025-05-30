from flask import jsonify
from sqlalchemy import func
from src.model.user import Leads, Users
from src.extensions.extensions import db


def add_user(user:Users):

    db.session.add(user)
    db.session.commit()


def update_user(user:Users):

    old_user = db.session.query(Users).filter_by(id=user.id).first()
    if(old_user):
        old_user.email = user.email
        old_user.name = user.name
        old_user.number = user.number
        db.session.commit()



def list_users():
    users = db.session.query(Users).all()
    return users


def create_leads():
    subquery = db.session.query(Leads.email).subquery()
    users = db.session.query(Users).filter(~Users.email.in_(subquery)).all()
    for user in users:
        obj = {'email':user.email, 'name':user.name, 'number':user.number, 'is_confirmed':user.is_confirmed}
        lead = Leads(email=obj['email'], name=obj['name'], number=obj['number'], is_confirmed=obj['is_confirmed'])
        db.session.add(lead)
        db.session.commit()
    
    





    


