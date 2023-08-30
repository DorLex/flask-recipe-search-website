from random import randint

from project.db_models import db, Recipes, Ingredients, Quantity, Book


def get_random_num():
    return randint(1, 25)


def save_to_db():
    for recipes_num in range(1, 16):
        recipes = Recipes(title=f'Рецепт {recipes_num}', description=f'описание рецепта {recipes_num} ' * 5)
        db.session.add(recipes)
        db.session.flush()

        for _ in range(5):
            ingredient_num = get_random_num()
            ingredient = Ingredients.query.filter_by(ingredient=f'ингредиент {ingredient_num}').first()
            if not ingredient:
                ingredient = Ingredients(ingredient=f'ингредиент {ingredient_num}')
            db.session.add(ingredient)
            db.session.flush()

            quantity_num = get_random_num()
            quantity = Quantity.query.filter_by(quantity=f'{quantity_num} кг').first()
            if not quantity:
                quantity = Quantity(quantity=f'{quantity_num}0 гр')
            db.session.add(quantity)
            db.session.flush()

            book = Book(recipe=recipes, ingredient=ingredient, quantity=quantity)
            db.session.add(book)
            db.session.flush()

        db.session.commit()
