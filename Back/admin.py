from flask import flash, redirect, session, url_for
from flask_admin import Admin, BaseView
from flask_admin.contrib.sqla import ModelView

from src.controller.flask_admin import ADMIN_PASSWORD, MyAdminIndexView
from src.model.date import Dates
from src.model.user import Users
from src.extensions.extensions import db



admin = Admin(name="Castro", template_mode="bootstrap3", index_view=MyAdminIndexView()) 

class AuthModelView(ModelView):

    def is_accessible(self):
        afirmative =  False
        authenticated = session.get("admin_authenticated")
        password_filled = session.get("admin_password_filled")

        if password_filled == ADMIN_PASSWORD and authenticated == True:
            afirmative = True
        
        return afirmative
    
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("admin_.login"))
    

class DateModelView(ModelView):
    column_list = [
        "id",
        "date",
        "total_amount",
    ]
    form_columns = ["total_amount"]

    can_create = False
    can_delete = True
    can_edit = True

    def on_model_change(self, form, model, is_created):
        if is_created:
            flash(f"Novo registro criado: {model}", "success")
        else:
            flash(f"Registro atualizado: {model}", "info")

    def on_model_delete(self, model):
        flash(f"Registro deletado: {model}", "danger")


class UserModelView(ModelView):

    column_list = [
        "id",
        "name",
        "email",
        "number",
        "message",
        "date",
        "budget",
    ]
    form_columns = [ 
        "name",
        "email",
        "number",
        "budget",]

    can_create = False
    can_delete = True
    can_edit = True

    def on_model_change(self, form, model, is_created):
        if is_created:
            flash(f"Novo registro criado: {model}", "success")
        else:
            flash(f"Registro atualizado: {model}", "info")

    def on_model_delete(self, model):
        flash(f"Registro deletado: {model}", "danger")


def init_app(app):
    with app.app_context():
        admin.init_app(app)
        admin.add_view(DateModelView(Dates, db.session))
        admin.add_view(UserModelView(Users, db.session))
