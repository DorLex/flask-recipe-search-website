from sqlalchemy import Select

from src.db_models import db, Recipes, Ingredients


def get_recipe_by_id(recipe_id: int) -> Recipes:
    query: Select = (
        db.select(Recipes)
        .filter_by(recipe_id=recipe_id)
    )
    recipe: Recipes = db.session.execute(query).scalar()

    return recipe


def get_recipes() -> list[Recipes]:
    query: Select = (
        db.select(Recipes)
        .order_by(Recipes.recipe_id.desc())
        .limit(7)
    )
    recipes: list[Recipes] = db.session.execute(query).scalars().unique().all()

    return recipes


def get_ingredients_ilike(ingredient: str) -> list[str]:
    query: Select = (
        db.select(Ingredients.title)
        .filter(
            Ingredients.title.ilike(f'%{ingredient}%'),
        )
    )

    ingredient_titles: list[str] = db.session.execute(query).scalars().all()

    return ingredient_titles
