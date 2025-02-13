from flask import request, jsonify
from flask.views import MethodView

from project.services import crud


class LiveSearchIngredients(MethodView):
    def get(self):
        input_ingredient = request.args.get('ingredient')
        ingredients_list = crud.get_ingredients_ilike(input_ingredient)

        return jsonify(ingredients_list)
