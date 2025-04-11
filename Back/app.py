import os
from flask import Flask
from flask_restful import Api
from flask_marshmallow import Marshmallow
import config
import pymysql
from flask_cors import CORS
from flask_migrate import Migrate
from src.extensions.extensions import db
from src.model.date import Dates
from src.model.user import Users
from admin import init_app as init_admin
from src.controller import flask_admin 




pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.secret_key = os.urandom(24)


app.debug = True

app.config.from_object(config.Config)
app.config['SQLALCHEMY_ECHO'] = True
ma = Marshmallow(app)
db.init_app(app)
migrate = Migrate(app, db)

api = Api(app)
CORS(app)

flask_admin.register_admin_routes(app)
init_admin(app)
