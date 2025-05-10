from datetime import datetime
from app import api
from flask import jsonify, request
from flask_restful import Resource
from src.schema.product_schema import ProductSchema
from src.model.date import Dates
from src.service.date import add_date
from src.service.product import list_products as lp
from src.model.products import  Products


class list_products(Resource):
     def get(self):
        products = lp()
        schema = ProductSchema(many=True)
        return jsonify(schema.dump(products))



api.add_resource(list_products, '/products')


