from src.models import Recipe
from src.repositories.recipe import RecipeRepository


class RecipeService:
    def __init__(self, repository: RecipeRepository) -> None:
        self.repository = repository

    def get_recipes(self) -> list[Recipe]:
        return self.repository.get_recipes()

    def get_recipe_by_id(self, recipe_id: int) -> Recipe:
        return self.repository.get_recipe_by_id(recipe_id)

    def get_ingredient_titles_ilike(self, title_fragment: str) -> list[str]:
        return self.repository.get_ingredient_titles_ilike(title_fragment)

    def get_recipes_by_ingredients(self, raw_ingredient_titles: str) -> list[Recipe]:
        ingredient_titles: list[str] = self._parse_ingredient_titles(raw_ingredient_titles)
        return self.repository.get_intersect_recipes(ingredient_titles)

    def _parse_ingredient_titles(self, raw_ingredient_titles: str) -> list[str]:
        return raw_ingredient_titles.split(',')
