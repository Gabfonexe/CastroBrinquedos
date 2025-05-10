from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from src.extensions.extensions import ma
from src.model.products import Products

class ProductSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Products
        load_instance = True

    id = ma.auto_field()
    quantity = ma.auto_field()
    is_available = ma.auto_field()
    price = ma.auto_field()

    # serializar o enum como string
    type = ma.Function(lambda obj: obj.type.value)