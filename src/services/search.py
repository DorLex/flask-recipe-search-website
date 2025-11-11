from sqlalchemy import Select, CompoundSelect

from src.db_models import db, Recipes, Ingredients


def _parse_search_elements(ingredients: str) -> list[str]:
    return ingredients.split(',')


def _generate_recipe_stmt_by_ingredient(ingredient: str) -> Select:
    recipes_id_stmt: Select = (
        db.select(Recipes.recipe_id)
        .join(Recipes.ingredients)
        .filter(Ingredients.title == ingredient)
    )

    return recipes_id_stmt


def _collect_recipe_stmts(search_elements: list[str]) -> list[Select]:
    return [_generate_recipe_stmt_by_ingredient(ingredient) for ingredient in search_elements]


def _get_intersect_recipes(intersect_recipes_id_query: CompoundSelect) -> list[Recipes]:
    query: Select = (
        db.select(Recipes)
        .filter(
            Recipes.recipe_id.in_(intersect_recipes_id_query),
        )
    )
    recipes: list[Recipes] = db.session.execute(query).scalars().unique().all()

    return recipes


def get_recipes_by_ingredients(ingredients: str) -> list[Recipes]:
    search_ingredients: list[str] = _parse_search_elements(ingredients)
    recipes_stmts: list[Select] = _collect_recipe_stmts(search_ingredients)
    intersect_recipes_id_query: CompoundSelect = db.intersect(*recipes_stmts)

    return _get_intersect_recipes(intersect_recipes_id_query)
