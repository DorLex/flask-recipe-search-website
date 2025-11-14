from flask import Response, jsonify, request
from flask.views import MethodView

from src.repositories.recipe import RecipeRepository
from src.services.recipe import RecipeService


class IngredientLiveSearchView(MethodView):
    def get(self) -> tuple[Response, int]:
        title_fragment: str | None = request.args.get('title_fragment')
        if not title_fragment:
            return jsonify({'error': 'title_fragment parameter is required'}), 422

        recipe_service: RecipeService = RecipeService(RecipeRepository())
        ingredient_titles: list[str] = recipe_service.get_ingredient_titles_ilike(title_fragment)

        return jsonify(ingredient_titles), 200
