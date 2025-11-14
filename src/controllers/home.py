from flask import render_template
from flask.views import MethodView

from src.models import Recipe
from src.repositories.recipe import RecipeRepository
from src.services.recipe import RecipeService


class HomeView(MethodView):
    def get(self) -> str:
        recipe_service: RecipeService = RecipeService(RecipeRepository())
        recipes: list[Recipe] = recipe_service.get_recipes()

        return render_template('index.html', recipes=recipes)
