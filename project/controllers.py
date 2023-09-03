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

    def get(self):
        input_ingredient = request.args.get('ingredient')
        print([input_ingredient])

        ingredients_obj = get_db.get_ingredients_ilike(input_ingredient)

        ingredients_list = []
        for ingredient in ingredients_obj:
            ingredients_list.append(ingredient.ingredient)

        return jsonify(ingredients_list)


class SearchRecipes(MethodView):
    def get(self):
        ingredients_str = request.args.get('ingredients')

        recipes_list = search.get_recipes_by_ingredients(ingredients_str)

        if not recipes_list:
            flash('НЕ НАЙДЕНО')

        return render_template('search.html', recipes=recipes_list, title='Поиск')


class About(MethodView):
    def get(self):
        return render_template('about.html', title='О сайте')
