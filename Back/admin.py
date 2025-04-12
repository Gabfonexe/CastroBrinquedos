from flask import flash, redirect, session, url_for
from flask_admin import Admin, BaseView
from flask_admin.contrib.sqla import ModelView
from wtforms import SelectField

from src.Enum import Types_Products
from src.controller.flask_admin import ADMIN_PASSWORD, MyAdminIndexView
from src.model.date import Dates
from src.model.user import Users
from src.model.calendar import Calendar
from src.model.products import Products
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


class CalendarModelView(ModelView):
    column_list = [
        "id",
        "date",
        "day_quantity",
    ]
    form_columns = [ 
        "day_quantity",        ]

    can_create = False
    can_delete = False
    can_edit = True

    def on_model_change(self, form, model, is_created):
        if is_created:
            flash(f"Novo registro criado: {model}", "success")
        else:
            flash(f"Registro atualizado: {model}", "info")

    def on_model_delete(self, model):
        flash(f"Registro deletado: {model}", "danger")


class ProductModelView(ModelView):

    form_overrides = dict(
        type=SelectField
    )

    def scaffold_form(self):
        form_class = super().scaffold_form()
        form_class.type = SelectField(
            'Type',
            choices=[(e.name, e.value) for e in Types_Products]
        )
        return form_class
    
    column_list = [
        "id",
        "type",
        "quantity",
    ]
    form_columns = [ 
        "quantity",
        "type",        ]

    can_create = True
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
        admin.add_view(CalendarModelView(Calendar, db.session))
        admin.add_view(ProductModelView(Products, db.session))
