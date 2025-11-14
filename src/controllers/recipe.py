from flask import render_template
from flask.views import MethodView

from src.models import Recipe
from src.repositories.recipe import RecipeRepository
from src.services.recipe import RecipeService


class RecipeView(MethodView):
    def get(self, recipe_id: int) -> str:
        recipe_service: RecipeService = RecipeService(RecipeRepository())
        recipe: Recipe = recipe_service.get_recipe_by_id(recipe_id)
        return render_template('recipe_details.html', recipe=recipe, title=f'Рецепт №{recipe_id}')
