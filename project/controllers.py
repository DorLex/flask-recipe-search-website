from flask import render_template, request, flash, jsonify
from flask.views import MethodView

from project.services import get_db, search


class HomeView(MethodView):
    def get(self):
        recipes = get_db.get_recipes()
        return render_template('index.html', recipes=recipes)


class RecipeDetails(MethodView):
    def get(self, recipe_id):
        recipe = get_db.get_recipe_by_id(recipe_id)
        return render_template('recipe_details.html', recipe=recipe, title=f'Рецепт №{recipe_id}')


class LiveSearchIngredients(MethodView):
    def post(self):
        json_data = request.get_json()
        ingredient = json_data.get('ingredient')

        ingredients = get_db.get_ingredients_ilike(ingredient)
        
        ingredients_list = []
        for ing in ingredients:
            ingredients_list.append(ing.ingredient)

        return jsonify(ingredients_list)


class SearchRecipes(MethodView):
    def get(self, ingredients):
        recipes_list = search.get_recipes_list(ingredients)
        if not recipes_list:
            flash('НЕ НАЙДЕНО')
        return render_template('search.html', recipes=recipes_list, title='Поиск')


class About(MethodView):
    def get(self):
        return render_template('about.html', title='О сайте')
