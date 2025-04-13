# Implementar lógica de verificar se o pedido foi confirmado e somar ou subtrair do amount + add no calendar
from datetime import datetime
from src.model.products import Products
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
            products = db.session.query(Products).filter(Products.type.name=='PULA_PULA_GRANDE')
            if is_date_exist:
                return
            new_calendar =  Calendar(convert_date)
            db.session.add(new_calendar)
    pass
#  Criar uma forma de retirar o amount se n estiver confirmado - Criar nova tabela de faturamento diário
# Criar rotina para devolver o valor da quantidade de cada produto após um determinado tempo.
