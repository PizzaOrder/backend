from models import addresses, order_items, orders, pizzas, promo_codes, users
from utils.database_orm import Base, engine

metadata = Base.metadata.create_all(engine)
