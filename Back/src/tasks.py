# Implementar lógica de verificar se o pedido foi confirmado e somar ou subtrair do amount + add no calendar
from datetime import date, datetime
import app
from src.model.products import Products
from src.extensions.extensions import db
from src.model.user import Users
from src.model.date import Dates
from src.model.calendar import Calendar, DateUnavailable
from src.Enum import Types_Products

# Talvez chamar esse método quando criar um novo user.
def amount_and_calendar_dayli_routine(): 
    #trocar para True dps
    # AQUI SÓ RODA NA PRIMEIRA VEZ DE 1 USER CONFIRMADO
    users = db.session.query(Users).filter(Users.is_confirmed == True and Users.is_checked == False).all() #criar nova coluna para verificar se o user ja foi verificado na rotina
    available_product_quantity = 0
    if users:
        for user in users:
            for product in user.products:
                product_type_enum = Types_Products(product['type'])
                exist_product = db.session.query(Products).filter(Products.type == product_type_enum).first() 
                if exist_product:
                    if exist_product.is_available == True:
                        exist_product.quantity -= product['quantity']
                        exist_product.lost_quantity += 1
                    if exist_product.quantity == 0:
                        exist_product.is_available = False
                        date_available_routine(user)
                        

            #Modularizar dps, criar uma function pra isso
            # date = datetime.strptime(user.date.replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f").date()
            exist_date = db.session.query(Calendar).filter(Calendar.date==user.date).first()
            products = db.session.query(Products).all()
            for product in products:
                available_product_quantity += product.quantity           
            if exist_date and user.is_checked == False:
                exist_date.day_quantity += 1 #MUDAR ISSO AQUI, MESMO USER Q JA FOI VERIFICADO, ESTÁ CAINDO AQUI NOVAMENTE (CONTABILIZANDO NA DIÁRIA DE ALUGUEL)
                if available_product_quantity == 0:
                    unavailable_date = DateUnavailable(date=user.date, reason='Todos os produtos foram alugados')
                    db.session.add(unavailable_date)
            
            new_calendar =  Calendar(date=user.date, day_quantity=1)
            db.session.add(new_calendar)

            #Preciso garantir que esse user n vai passar novamente na condição do SQL expression acima
            




# criar método para o produto voltar a ser available, chamar ele antes do amount_and_calendar_dayli_routine
def date_available_routine(user:Users):
    now = datetime.now().date()
    # user_date = datetime.strptime(user.date.replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f").date()
    difference_days = (user.date - now).days
    
    if  difference_days <= 0:
        for product in user.products:
            product_type_enum = Types_Products(product['type'])
            exist_product = db.session.query(Products).filter(Products.type == product_type_enum).first()
            if exist_product:
                exist_product.quantity += product['quantity']
                exist_product.lost_quantity -= product['quantity']
                exist_product.is_available = True
                user.is_checked = True
        return True
    return False








# Criar uma forma de retirar o amount se n estiver confirmado - Criar nova tabela de faturamento diário
# Criar rotina para devolver o valor da quantidade de cada produto após um determinado tempo.
