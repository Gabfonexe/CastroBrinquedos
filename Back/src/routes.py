from src.controller.product import list_products
from src.controller.user import  Add_User, list_users, Update_User
from src.controller.dates import Unavailable_Dates
from src.controller.castro import Start_App

def register_routes(api):
    api.add_resource(list_products, '/products')
    api.add_resource(Add_User, '/criar')
    api.add_resource(list_users, '/users')
    api.add_resource(Update_User, '/alterar')
    api.add_resource(Unavailable_Dates, '/unavailable/dates')
    api.add_resource(Start_App, '/')

   
