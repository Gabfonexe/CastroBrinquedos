from datetime import datetime
from app import api
from flask import jsonify, request
from flask_restful import Resource
from src.model.date import Dates
from src.service.date import add_date
from src.service.product import list_products
from src.model.products import Products


class list_products(Resource):
     def get(self):
        products = list_products()
        return jsonify(products)



api.add_resource(list_products, '/products')


