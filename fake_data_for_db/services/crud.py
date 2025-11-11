from sqlalchemy import Select

from src.db_models import Recipes, Ingredients, db


def create_recipe(recipes_num: int) -> Recipes:
    return Recipes(
        title=f'Рецепт {recipes_num}',
        description=f'описание рецепта {recipes_num} ' * 50,
    )


def _get_ingredient(ingredient_num: int) -> Ingredients | None:
    query: Select = (
        db.select(Ingredients)
        .filter_by(title=f'ингредиент {ingredient_num}')
    )
    ingredient: Ingredients | None = db.session.execute(query).scalar()

    return ingredient


def _create_ingredient(ingredient_num: int) -> Ingredients:
    return Ingredients(
        title=f'ингредиент {ingredient_num}',
        weight=f'{ingredient_num}0 гр',
    )


def get_or_create_ingredient(ingredient_num: int) -> Ingredients:
    return _get_ingredient(ingredient_num) or _create_ingredient(ingredient_num)
