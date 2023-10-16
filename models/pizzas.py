from sqlalchemy import Integer, String, Column, DateTime, ForeignKey
from utils.database_orm import Base



# Table Pizzas {
#   pizza_id int [pk] //
#   default_pizza_id string [ref: > DefaultPizza.pizza_id] // Любая пицца из DefaultPizza
#   first_part string
#   second_part string
#   third_part string
#   fourth_part string
#   total_cost decimal [not null]
# }

class Pizza(Base):
    __tablename__ = 'pizzas'

    pizza_id = Column(Integer, primary_key=True)
    default_pizza_id = Column(Integer, ForeignKey('pizzas.id'))
