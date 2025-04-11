from flask import jsonify
from src.model.user import Users
from src.extensions.extensions import db


def add_user(user:Users):

    exists_user = db.session.query(Users).filter_by(email=user.email, number=user.number).first()
    if(exists_user):
        return jsonify({"error":"Esse usuário já foi cadastrado"})
    
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
