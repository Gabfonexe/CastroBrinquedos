# Implementar lógica de verificar se o pedido foi confirmado e somar ou subtrair do amount + add no calendar
from datetime import date, datetime

from sqlalchemy import and_
import app
from src.model.products import Products
from src.extensions.extensions import db
from src.model.user import Users
from src.model.date import Dates
from src.model.calendar import Calendar, DateUnavailable
from src.Enum import Types_Products
import threading
import time

# Talvez chamar esse método quando criar um novo user.
def amount_and_calendar_dayli_routine(): 
    #trocar para True dps
    # AQUI SÓ RODA NA PRIMEIRA VEZ DE 1 USER CONFIRMADO
    while True:
        try:
            with app.app.app_context():
                now = datetime.now().date()
                users = db.session.query(Users).filter(and_(Users.is_confirmed == True, Users.is_checked == False)).all() #criar nova coluna para verificar se o user ja foi verificado na rotina
                available_product_quantity = 0
                print("🕒 Rodando rotina...")
                if users:
                    for user in users:
                        for product in user.products:
                            product_type_enum = Types_Products(product['type'])
                            exist_product = db.session.query(Products).filter(Products.type == product_type_enum).first() 
                            if exist_product:
                                if exist_product.is_available == True:
                                     # mudar para colocar a data do futuro e n no presente.
                                    exist_product.quantity -= product['quantity']
                                    exist_product.lost_quantity += 1
                                    db.session.commit()
                                if exist_product.quantity == 0:
                                    exist_product.is_available = False
                                    unavailable_date = DateUnavailable(date=user.date, reason=f'O produto {exist_product.type.value} ficou indisponível', product=exist_product.type.value)
                                    db.session.add(unavailable_date)
                                    date_available_routine(user)
                                    db.session.commit()
                                    
                        exist_date = db.session.query(Calendar).filter(Calendar.date==user.date).first()

                        products = db.session.query(Products).all()
                        for product in products:
                            available_product_quantity += product.quantity 
                        if available_product_quantity == 0:
                            unavailable_date = DateUnavailable(date=user.date, reason='Todos os produtos foram alugados')
                            db.session.add(unavailable_date)
                            db.session.commit()
                        if exist_date and user.is_dayli_confirmed == False:
                            exist_date.day_quantity += 1 
                            db.session.commit()
                        elif not exist_date:
                            new_calendar =  Calendar(date=user.date, day_quantity=1)
                            user.is_dayli_confirmed = True
                            db.session.add(new_calendar)
                            db.session.commit()
                       

        except Exception as e:
            print(e)
        print("🕒 Fim da rotina...")
        time.sleep(6 * 60 * 60)
        
        # CRIAR UMA LISTA DE HORÁRIOS, PARA ESCOLHER O HORÁRIO ESPECÍFICO
            
            # DEIXAR UNAVALABLE SOMENTE NA DATA QUE FOI ESCOLHIDA


def date_available_routine(user:Users):
    now = datetime.now().date()
    difference_days = (user.date - now).days
    
    if  difference_days <= -1: #TODO SE FOR INFLAVEL, PODE SER <= 0, verificar isso ainda.
        for product in user.products:
            product_type_enum = Types_Products(product['type'])
            exist_product = db.session.query(Products).filter(Products.type == product_type_enum).first()
            if exist_product:
                exist_product.quantity += product['quantity']
                exist_product.lost_quantity -= product['quantity']
                exist_product.is_available = True
                user.is_checked = True
                db.session.commit()
        return True
    return False


# Criar uma forma de retirar o amount se n estiver confirmado - Criar nova tabela de faturamento diário
# Criar rotina para devolver o valor da quantidade de cada produto após um determinado tempo.
