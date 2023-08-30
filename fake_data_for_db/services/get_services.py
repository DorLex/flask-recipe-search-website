from project.db_models import Ingredients, Quantity


def get_ingredient(ingredient_num):
    ingredient = Ingredients.query.filter_by(ingredient=f'ингредиент {ingredient_num}').first()
    return ingredient


def get_quantity(quantity_num):
    quantity = Quantity.query.filter_by(quantity=f'{quantity_num}0 гр').first()
    return quantity
