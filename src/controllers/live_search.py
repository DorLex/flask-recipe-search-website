from flask import Response, jsonify, request
from flask.views import MethodView

from src.repositories.recipe import RecipeRepository
from src.services.recipe import RecipeService


class IngredientLiveSearchView(MethodView):
    def get(self) -> Response:
        title_fragment: str = request.args.get('title_fragment')

        recipe_service: RecipeService = RecipeService(RecipeRepository())
        ingredient_titles: list[str] = recipe_service.get_ingredient_titles_ilike(title_fragment)

        return jsonify(ingredient_titles)
