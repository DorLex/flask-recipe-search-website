from project.db_models import Recipes, Ingredients, Quantity, Book


def create_recipe(recipes_num):
    recipes = Recipes(title=f'Рецепт {recipes_num}', description=f'описание рецепта {recipes_num} ' * 5)
    return recipes


def create_ingredient(ingredient_num):
    ingredient = Ingredients(ingredient=f'ингредиент {ingredient_num}')
    return ingredient


def create_quantity(quantity_num):
    quantity = Quantity(quantity=f'{quantity_num}0 гр')
    return quantity


def create_book(recipe, ingredient, quantity):
    book = Book(recipe=recipe, ingredient=ingredient, quantity=quantity)
    return book
