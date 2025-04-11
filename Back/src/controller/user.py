from datetime import datetime
from app import api
from flask import jsonify, request
from flask_restful import Resource
from src.model.date import Dates
from src.service.date import add_date
from src.service import user as user_service
from src.model.user import Users

class Login():
    pass


class Add_User(Resource):
    def post(self):
        data = request.get_json()
        user = Users(email=data['email'], number=data['phone'], name=data['name'], message=data['message'], date=data['date'], budget=data['amount'])
        user_service.add_user(user)

        raw_date = data['date']
        parsed_date = datetime.fromisoformat(raw_date.replace("Z", "")).date()
        date_obj = Dates(date=parsed_date, total_amount=data['amount'])
        add_date(date_obj)
        return {"message": "Data registrada com sucesso"}, 201

class Update_User(Resource):
    def put(self):
        data = request.get_json()
        user = Users(email=data['email'], number=data['number'], name=data['name'], id=data['id'])
        user_release = user_service.update_user(user)
        return jsonify(user_release)

class list_users(Resource):
     def get(self):
        users = user_service.list_users()
        return jsonify(users)


api.add_resource(Add_User, '/criar')
api.add_resource(list_users, '/users')
api.add_resource(Update_User, '/alterar')

