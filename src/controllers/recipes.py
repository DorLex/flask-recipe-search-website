from flask import flash, render_template, request
from flask.views import MethodView

from src.db_models import Recipes
from src.services import crud, search


class RecipeDetails(MethodView):
    def get(self, recipe_id: int) -> str:
        recipe: Recipes = crud.get_recipe_by_id(recipe_id)
        return render_template('recipe_details.html', recipe=recipe, title=f'Рецепт №{recipe_id}')


class SearchRecipes(MethodView):
    def get(self) -> str:
        ingredients: str = request.args.get('ingredients')
        recipes: list[Recipes] = search.get_recipes_by_ingredients(ingredients)

        if not recipes:
            flash('НЕ НАЙДЕНО')

        return render_template('search.html', recipes=recipes, title='Поиск')
