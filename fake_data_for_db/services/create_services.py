from project.db_models import Recipes, Ingredients


def create_recipe(recipes_num):
    recipes = Recipes(title=f'Рецепт {recipes_num}', description=f'описание рецепта {recipes_num} ' * 5)
    return recipes


def create_ingredient(ingredient_num):
    ingredient = Ingredients(title=f'ингредиент {ingredient_num}', weight=f'{ingredient_num}0 гр')
    return ingredient
