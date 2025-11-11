from flask import request, jsonify
from flask.views import MethodView

from src.services import crud


class LiveSearchIngredients(MethodView):
    def get(self):
        input_ingredient: str = request.args.get('ingredient')
        ingredients: list[str] = crud.get_ingredients_ilike(input_ingredient)

        return jsonify(ingredients)
