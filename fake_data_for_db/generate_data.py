from fake_data_for_db.services.crud import create_recipe, get_or_create_ingredient
from fake_data_for_db.services.randomizer import get_ingredient_num
from src.db_models import db, Recipes, Ingredients


def _save(obj: db.Model) -> None:
    db.session.add(obj)
    db.session.flush()


def save_fake_data_to_db() -> None:
    for recipes_num in range(1, 16):
        recipe: Recipes = create_recipe(recipes_num)
        _save(recipe)

        used_numbers = set()
        for _ in range(5):
            ingredient_num: int = get_ingredient_num(used_numbers)

            ingredient: Ingredients = get_or_create_ingredient(ingredient_num)
            _save(ingredient)

            recipe.ingredients.append(ingredient)

        db.session.commit()
