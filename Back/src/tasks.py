
from datetime import date, datetime

from sqlalchemy import and_
import app
from src.service.date import add_date
from src.model.products import Products
from src.extensions.extensions import db
from src.model.user import Users
from src.model.date import Dates
from src.model.calendar import Calendar, DateUnavailable
from src.Enum import Types_Products


def amount_and_calendar_dayli_routine(): 
        with app.app.app_context():
            
            try:
                users = db.session.query(Users).filter(and_(Users.is_confirmed == True, Users.is_checked == False)).all() 
                available_product_quantity = 0
                print("🕒 Rodando rotina...")
                if users:            
                    for user in users:
                        for product in user.products:
                            product_type_enum = Types_Products(product['type'])
                            exist_product = db.session.query(Products).filter(Products.type == product_type_enum).first() 
                            if exist_product:
                                if exist_product.is_available == True:
                                    exist_product.quantity -= product['quantity']
                                    exist_product.lost_quantity += 1
                                    db.session.commit()
                                if exist_product.quantity == 0:
                                    exist_product.is_available = False
                                    unavailable_date = DateUnavailable(date=user.date, reason=f'O produto {exist_product.type.value} ficou indisponível', product=exist_product.type.value)
                                    db.session.add(unavailable_date)
                                    date_available_routine(user)
                                    db.session.commit()
                                    
                        exist_calendar = db.session.query(Calendar).filter(Calendar.date==user.date).first()
                        exist_date = db.session.query(Dates).filter(Dates.date==user.date).first()

                        products = db.session.query(Products).all()
                        for product in products:
                            available_product_quantity += product.quantity 
                        if available_product_quantity == 0:
                            unavailable_date = DateUnavailable(date=user.date, reason='Todos os produtos foram alugados')
                            db.session.add(unavailable_date)
                            
                        if exist_calendar and user.is_dayli_confirmed == False:
                            exist_calendar.day_quantity += 1 
                            user.is_dayli_confirmed = True
                            
                        elif not exist_calendar:
                            new_calendar =  Calendar(date=user.date, day_quantity=1)
                            user.is_dayli_confirmed = True
                            db.session.add(new_calendar)
                            
                        if exist_date and user.is_dayli_confirmed == False:
                            exist_date.total_amount += user.budget
                            user.is_dayli_confirmed = True
                            
                        elif not exist_date:
                            new_date = Dates(date=user.date, total_amount=user.budget)
                            user.is_dayli_confirmed = True
                            add_date(new_date) 
                        db.session.commit()    
                       

            except Exception as e:
                print(e)
            print("🕒 Fim da rotina...")
        
            



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

