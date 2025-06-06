from datetime import datetime
from flask import jsonify, request
from flask_restful import Resource
from src.model.date import Dates
from src.service.date import add_date
from src.service import user as user_service
from src.model.user import Users
from src.tasks import amount_and_calendar_dayli_routine

class Login():
    pass


class Add_User(Resource):
    def post(self):
        data = request.get_json()
        user_date = datetime.strptime(data['date'].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f").date()
        user = Users(email=data['email'], number=data['phone'], name=data['name'], message=data['message'], date=user_date, budget=data['amount'], products=data['products'])
        user_service.add_user(user)
        user_service.create_leads()
        amount_and_calendar_dayli_routine()
    
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
     


