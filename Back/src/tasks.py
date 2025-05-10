# Implementar lógica de verificar se o pedido foi confirmado e somar ou subtrair do amount + add no calendar
from datetime import date, datetime
import app
from src.model.products import Products
from src.extensions.extensions import db
from src.model.user import Users
from src.model.date import Dates
from src.model.calendar import Calendar
from src.Enum import Types_Products

# Talvez chamar esse método quando criar um novo user.
def amount_and_calendar_dayli_routine(): 
    #trocar para True dps
    # AQUI SÓ RODA NA PRIMEIRA VEZ DE 1 USER CONFIRMADO
    users = db.session.query(Users).filter(Users.is_confirmed == False and Users.is_checked == False).all() #criar nova coluna para verificar se o user ja foi verificado na rotina
    available_product_quantity = 0
    if users:
        for user in users:
            for product in user.products:
                exist_product = db.session.query(Products).filter(Products.type==product['name']).first() # não preciso mudar, pq no futuro o front vai pegar os produtos diretamente do DB, por isso o type vai ser sempre igual
                if exist_product:
                    exist_product.quantity - product['quantity'] #preciso voltar a quantidade original de produtos depois
                    exist_product.lost_quantity += 1
                    if exist_product.quantity == 0:
                        exist_product.is_available = False
                        response = date_available_routine(user)
                        if response == True:
                            #Preciso setar de alguma forma, um valor padrão de quantidade ou verificar quantas vezes o quantity foi subtraído
                            exist_product.is_available = True
                        #Tornar available depois da data da festa - chamar o date_avaialble_routine aqui
            #Mudar aqui embaixo
            date = datetime.strptime(user.date.replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f").date()
            exist_date = db.session.query(Calendar).filter(Calendar.date==date).first()
            products = db.session.query(Products).all()
            for product in products:
                available_product_quantity += product.quantity           

            if exist_date:
                return
            new_calendar =  Calendar(date)
            db.session.add(new_calendar)

            #Preciso garantir que esse user n vai passar novamente na condição do SQL expression acima
            
    pass



# criar método para o produto voltar a ser available, chamar ele antes do amount_and_calendar_dayli_routine
def date_available_routine(user:Users):
    now = datetime.now().date()
    user_date = datetime.strptime(user.date.replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f").date()
    difference_days = (user_date - now).days
    
    if  difference_days <= 0:
        for product in user.products:
            exist_product = db.session.query(Products).filter(Products.type==product['name']).first()
            if exist_product:
                exist_product.quantity += product['quantity']
                exist_product.lost_quantity -= product['quantity']
                exist_product.is_available = True
                user.is_checked = True
        return True
    return False








# Criar uma forma de retirar o amount se n estiver confirmado - Criar nova tabela de faturamento diário
# Criar rotina para devolver o valor da quantidade de cada produto após um determinado tempo.
