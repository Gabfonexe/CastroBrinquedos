from src.model.products import Products
from src.extensions.extensions import db


def list_products():
    products = db.session.query(Products).all()
    return products
