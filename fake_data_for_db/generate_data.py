from fake_data_for_db.generate_services.create_services import create_recipe
from fake_data_for_db.generate_services.get_services import get_or_create_ingredient
from fake_data_for_db.generate_services.random_services import get_ingredient_num
from project.db_models import db


def _save(obj):
    db.session.add(obj)
    db.session.flush()


def save_fake_data_to_db():
    for recipes_num in range(1, 16):
        recipe = create_recipe(recipes_num)
        _save(recipe)

        used_numbers = dict()
        for _ in range(1, 6):
            ingredient_num = get_ingredient_num(used_numbers)

            ingredient = get_or_create_ingredient(ingredient_num)
            _save(ingredient)

            recipe.ingredients.append(ingredient)

        db.session.commit()
