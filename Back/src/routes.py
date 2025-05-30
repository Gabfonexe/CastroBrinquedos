from src.controller.product import list_products
from src.controller.user import  Add_User, list_users, Update_User
from src.controller.dates import Unavailable_Dates

def register_routes(api):
    api.add_resource(list_products, '/products')
    api.add_resource(Add_User, '/products')
    api.add_resource(list_users, '/products')
    api.add_resource(Update_User, '/products')
    api.add_resource(Unavailable_Dates, '/products')

   
