from flask import flash, render_template, request
from flask.views import MethodView

from src.models import Recipe
from src.repositories.recipe import RecipeRepository
from src.services.recipe import RecipeService


class RecipeSearchView(MethodView):
    def get(self) -> str:
        ingredients: str = request.args.get('ingredients')

        recipe_service: RecipeService = RecipeService(RecipeRepository())
        recipes: list[Recipe] = recipe_service.get_recipes_by_ingredients(ingredients)

        if not recipes:
            flash('НЕ НАЙДЕНО')

        return render_template('search.html', recipes=recipes, title='Поиск')
