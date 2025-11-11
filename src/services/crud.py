from sqlalchemy import Select

from src.db_models import Ingredient, Recipe, db


def get_recipe_by_id(recipe_id: int) -> Recipe:
    query: Select = db.select(Recipe).where(Recipe.id == recipe_id)
    recipe: Recipe = db.session.execute(query).scalar()

    return recipe


def get_recipes() -> list[Recipe]:
    query: Select = db.select(Recipe).order_by(Recipe.id.desc()).limit(7)
    recipes: list[Recipe] = db.session.execute(query).scalars().unique().all()

    return recipes


def get_ingredients_ilike(ingredient: str) -> list[str]:
    query: Select = db.select(Ingredient.title).where(Ingredient.title.ilike(f'%{ingredient}%'))
    ingredient_titles: list[str] = db.session.execute(query).scalars().all()

    return ingredient_titles
