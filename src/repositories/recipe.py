from sqlalchemy import CompoundSelect, Select

from src.core.database import db
from src.models import Ingredient, Recipe


class RecipeRepository:
    def get_recipes(self) -> list[Recipe]:
        query: Select = db.select(Recipe).order_by(Recipe.id.desc()).limit(7)
        recipes: list[Recipe] = db.session.execute(query).scalars().unique().all()
        return recipes

    def get_recipe_by_id(self, recipe_id: int) -> Recipe:
        query: Select = db.select(Recipe).where(Recipe.id == recipe_id)
        recipe: Recipe = db.session.execute(query).scalar()
        return recipe

    def get_ingredient_titles_ilike(self, title_fragment: str) -> list[str]:
        query: Select = db.select(Ingredient.title).where(Ingredient.title.ilike(f'%{title_fragment}%'))
        ingredient_titles: list[str] = db.session.execute(query).scalars().all()
        return ingredient_titles

    def get_intersect_recipes(self, ingredient_titles: list[str]) -> list[Recipe]:
        recipes_ids_intersect_stmt: CompoundSelect = self._collect_recipe_stmts(ingredient_titles)

        query: Select = db.select(Recipe).where(Recipe.id.in_(recipes_ids_intersect_stmt))
        recipes: list[Recipe] = db.session.execute(query).scalars().unique().all()

        return recipes

    def _collect_recipe_stmts(self, ingredient_titles: list[str]) -> CompoundSelect:
        recipe_id_stmts: list[Select[list[int]]] = [
            self._get_recipe_stmt_by_ingredient(ingredient_title) for ingredient_title in ingredient_titles
        ]
        return db.intersect(*recipe_id_stmts)

    def _get_recipe_stmt_by_ingredient(self, ingredient_title: str) -> Select[list[int]]:
        return db.select(Recipe.id).join(Recipe.ingredients).where(Ingredient.title == ingredient_title)
