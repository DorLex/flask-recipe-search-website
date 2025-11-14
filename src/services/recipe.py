from sqlalchemy import CompoundSelect, Select

from src.core.database import db
from src.models import Recipe
from src.repositories.recipe import RecipeRepository
from src.services.search import _collect_recipe_stmts, _get_intersect_recipes, _parse_search_elements


class RecipeService:
    def __init__(self, repository: RecipeRepository) -> None:
        self.repository = repository

    def get_recipes(self) -> list[Recipe]:
        return self.repository.get_recipes()

    def get_recipe_by_id(self, recipe_id: int) -> Recipe:
        return self.repository.get_recipe_by_id(recipe_id)

    def get_ingredient_titles_ilike(self, title_fragment: str) -> list[str]:
        return self.repository.get_ingredient_titles_ilike(title_fragment)

    def get_recipes_by_ingredients(self, ingredients: str) -> list[Recipe]:
        search_ingredients: list[str] = _parse_search_elements(ingredients)
        recipes_stmts: list[Select] = _collect_recipe_stmts(search_ingredients)
        intersect_recipes_id_query: CompoundSelect = db.intersect(*recipes_stmts)

        return _get_intersect_recipes(intersect_recipes_id_query)
