# Implementar lógica de verificar se o pedido foi confirmado e somar ou subtrair do amount + add no calendar
from datetime import datetime
from extensions.extensions import db
from src.model.user import Users
from src.model.date import Dates
from src.model.calendar import Calendar

# Talvez chamar esse método quando criar um novo user.
def amount_and_calendar_dayli_routine():

    users = db.session.query(Users).filter(Users.is_confirmed == True).all()
    if users:
        for user in users:
            convert_date = user.date
            is_date_exist = db.session.query(Calendar).filter(Calendar.date==convert_date).first()
            if is_date_exist:
                return
            new_calendar =  Calendar(convert_date)
            db.session.add(new_calendar)
    pass