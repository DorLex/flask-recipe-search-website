from random import randint

from fake_data_for_db.services.create_services import create_recipe
from fake_data_for_db.services.get_services import get_or_create_ingredient
from project.db_models import db


def _get_random_num():
    random_num = randint(1, 10)
    return random_num


def _get_ingredient_num(ingredients_map):
    while True:
        random_num = _get_random_num()
        if random_num not in ingredients_map:
            ingredient_num = random_num
            ingredients_map.append(random_num)

            return ingredient_num

        else:
            continue


def save(obj):
    db.session.add(obj)
    db.session.flush()


def save_data_to_db():
    for recipes_num in range(1, 16):
        recipe = create_recipe(recipes_num)
        save(recipe)

        ingredients_map = []
        for _ in range(1, 6):
            ingredient_num = _get_ingredient_num(ingredients_map)

            ingredient = get_or_create_ingredient(ingredient_num)
            save(ingredient)

            recipe.ingredients.append(ingredient)

        db.session.commit()
