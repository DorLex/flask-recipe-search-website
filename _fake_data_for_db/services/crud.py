# from sqlalchemy import Select
#
# from src.db_models import Ingredient, Recipe, db
#
#
# def create_recipe(recipes_num: int) -> Recipe:
#     return Recipe(
#         title=f'Рецепт {recipes_num}',
#         description=f'описание рецепта {recipes_num} ' * 50,
#     )
#
#
# def _get_ingredient(ingredient_num: int) -> Ingredient | None:
#     query: Select = db.select(Ingredient).filter_by(title=f'ингредиент {ingredient_num}')
#     ingredient: Ingredient | None = db.session.execute(query).scalar()
#
#     return ingredient
#
#
# def _create_ingredient(ingredient_num: int) -> Ingredient:
#     return Ingredient(
#         title=f'ингредиент {ingredient_num}',
#         weight=f'{ingredient_num}0 гр',
#     )
#
#
# def get_or_create_ingredient(ingredient_num: int) -> Ingredient:
#     return _get_ingredient(ingredient_num) or _create_ingredient(ingredient_num)
