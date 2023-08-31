from flask import render_template, request, flash, jsonify
from flask.views import MethodView

from project.db_models import db, Recipes, Ingredients, Book
from project.services import get_db


class HomeView(MethodView):
    def get(self):
        recipes = get_db.get_recipes()
        return render_template('index.html', recipes=recipes)


class RecipeDetails(MethodView):
    def get(self, recipe_id):
        recipe = get_db.get_recipe(recipe_id)
        return render_template('recipe_details.html', recipe=recipe, title=f'Рецепт №{recipe_id}')


class About(MethodView):
    def get(self):
        return render_template('about.html', title='О сайте')


class LiveSearchIngredients(MethodView):
    def post(self):
        json_data = request.get_json()
        ingredients = get_db.get_ingredients(json_data)
        ingredients_list = []
        for ing in ingredients:
            ingredients_list.append(ing.ingredient)

        return jsonify(ingredients_list)


class SearchRecipes(MethodView):
    def get(self, ingredients):
        if ingredients:
            recipes = Searcher.result(ingredients)
            if not recipes:
                flash('НЕ НАЙДЕНО')
            return render_template('search.html', recipes=recipes, title='Поиск')
        else:
            return render_template('search.html', recipes=None, title='Поиск')


class Searcher:
    @classmethod
    def search_for_recipe_matches(cls, intersect_recipes_id_query):
        recipes = Recipes.query.filter(Recipes.id.in_(intersect_recipes_id_query)).all()
        return recipes

    @classmethod
    def intersect_recipes_id(cls, query_objs):
        result = db.intersect(*query_objs)
        return result

    @classmethod
    def search_recipes_id_by_ingredients(cls, search_elements):
        query_objs = []  # list[query,] query() -> [(1,), (2,),]   (query на каждый ингредиент)
        for ing in search_elements:
            ingredient_with_recipes = db.session.query(Recipes.id) \
                .join(Book, Book.recipe_id == Recipes.id) \
                .join(Ingredients, Book.ingredient_id == Ingredients.id) \
                .filter(Ingredients.ingredient.ilike(f'%{ing}%'))
            query_objs.append(ingredient_with_recipes)

        return query_objs

    @classmethod
    def get_search_elements(cls, q):
        # search_elements = [x.strip() for x in q.split(',')]
        search_elements = q.strip().split(',')
        return search_elements

    @classmethod
    def result(cls, q):
        search_elements = cls.get_search_elements(q)
        query_objs = cls.search_recipes_id_by_ingredients(search_elements)
        intersect_recipes_id_query = cls.intersect_recipes_id(query_objs)
        recipes = cls.search_for_recipe_matches(intersect_recipes_id_query)

        return recipes
