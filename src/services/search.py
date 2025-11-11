from sqlalchemy import CompoundSelect, Select

from src.db_models import Ingredient, Recipe, db


def _parse_search_elements(ingredients: str) -> list[str]:
    return ingredients.split(',')


def _generate_recipe_stmt_by_ingredient(ingredient: str) -> Select:
    return db.select(Recipe.id).join(Recipe.ingredients).where(Ingredient.title == ingredient)


def _collect_recipe_stmts(search_elements: list[str]) -> list[Select]:
    return [_generate_recipe_stmt_by_ingredient(ingredient) for ingredient in search_elements]


def _get_intersect_recipes(intersect_recipes_id_query: CompoundSelect) -> list[Recipe]:
    query: Select = db.select(Recipe).where(Recipe.id.in_(intersect_recipes_id_query))
    recipes: list[Recipe] = db.session.execute(query).scalars().unique().all()
    return recipes


def get_recipes_by_ingredients(ingredients: str) -> list[Recipe]:
    search_ingredients: list[str] = _parse_search_elements(ingredients)
    recipes_stmts: list[Select] = _collect_recipe_stmts(search_ingredients)
    intersect_recipes_id_query: CompoundSelect = db.intersect(*recipes_stmts)

    return _get_intersect_recipes(intersect_recipes_id_query)
