from flask import jsonify
from flask_restful import Resource
from src.service.unavailable_dates import list_dates_unavailables
from app import api

class Unavailable_Dates(Resource):
    def get(self):
        dates = list_dates_unavailables()
        return jsonify(dates)
    
api.add_resource(Unavailable_Dates, '/unavailable/dates')