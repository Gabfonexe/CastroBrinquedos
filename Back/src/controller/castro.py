from flask import jsonify
from flask_restful import Resource


class Start_App(Resource):
    def get(self):
        
        return jsonify({'message': 'App rodando'})