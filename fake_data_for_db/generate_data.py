from fake_data_for_db.services.create_services import create_recipe, create_relationship
from fake_data_for_db.services.service import get_or_create_ingredient, get_or_create_quantity
from project.db_models import db


def save(obj):
    db.session.add(obj)
    db.session.flush()


def save_data_to_db():
    for recipes_num in range(1, 16):
        recipe = create_recipe(recipes_num)
        save(recipe)

        for _ in range(5):
            ingredient = get_or_create_ingredient()
            save(ingredient)

            quantity = get_or_create_quantity()
            save(quantity)

            relationship = create_relationship(recipe, ingredient, quantity)
            save(relationship)

        db.session.commit()
