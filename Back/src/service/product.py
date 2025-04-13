from src.model.products import Products
from src.extensions.extensions import db


def list_products():
    users = db.session.query(Products).all()
    return users
