from flask import Response, jsonify, request
from flask.views import MethodView

from src.services import crud


class LiveSearchIngredients(MethodView):
    def get(self) -> Response:
        input_ingredient: str = request.args.get('ingredient')
        ingredients: list[str] = crud.get_ingredients_ilike(input_ingredient)

        return jsonify(ingredients)
