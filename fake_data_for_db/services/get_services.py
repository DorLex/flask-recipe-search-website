from fake_data_for_db.services.create_services import create_ingredient
from project.db_models import Ingredients, db


def _get_ingredient(ingredient_num):
    ingredient = db.session.execute(
        db.select(Ingredients).filter_by(title=f'ингредиент {ingredient_num}')
    ).scalar()

    return ingredient


def get_or_create_ingredient(ingredient_num):
    ingredient = _get_ingredient(ingredient_num) or create_ingredient(ingredient_num)
    return ingredient
