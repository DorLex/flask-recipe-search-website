from flask import render_template, request, flash
from flask.views import MethodView

from project.services import crud, search


class RecipeDetails(MethodView):
    def get(self, recipe_id):
        recipe = crud.get_recipe_by_id(recipe_id)
        return render_template('recipe_details.html', recipe=recipe, title=f'Рецепт №{recipe_id}')


class SearchRecipes(MethodView):
    def get(self):
        ingredients_str = request.args.get('ingredients')
        recipes_list = search.get_recipes_by_ingredients(ingredients_str)

        if not recipes_list:
            flash('НЕ НАЙДЕНО')

        return render_template('search.html', recipes=recipes_list, title='Поиск')
