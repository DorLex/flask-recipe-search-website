from flask import flash, render_template, request
from flask.views import MethodView

from src.models import Recipe
from src.repositories.recipe import RecipeRepository
from src.services.recipe import RecipeService


class RecipeSearchView(MethodView):
    def get(self) -> str:
        raw_ingredient_titles: str | None = request.args.get('ingredients')
        if not raw_ingredient_titles:
            flash('Неверно переданы названия ингредиентов')
            return render_template('search.html', recipes=[], title='Поиск')

        recipe_service: RecipeService = RecipeService(RecipeRepository())
        recipes: list[Recipe] = recipe_service.get_recipes_by_ingredients(raw_ingredient_titles)

        if not recipes:
            flash('НЕ НАЙДЕНО')
        return render_template('search.html', recipes=recipes, title='Поиск')
