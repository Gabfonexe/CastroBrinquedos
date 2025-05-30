from flask import jsonify
from flask_restful import Resource
from src.service.unavailable_dates import list_dates_unavailables


class Unavailable_Dates(Resource):
    def get(self):
        dates = list_dates_unavailables()
        return jsonify(dates)
    
