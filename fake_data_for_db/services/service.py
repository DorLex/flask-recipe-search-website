from random import randint

from fake_data_for_db.services.create_services import create_ingredient, create_quantity
from fake_data_for_db.services.get_services import get_ingredient, get_quantity


def get_random_num():
    return randint(1, 25)


def get_or_create_ingredient():
    ingredient_num = get_random_num()
    ingredient = get_ingredient(ingredient_num) or create_ingredient(ingredient_num)
    return ingredient


def get_or_create_quantity():
    quantity_num = get_random_num()
    quantity = get_quantity(quantity_num) or create_quantity(quantity_num)
    return quantity
