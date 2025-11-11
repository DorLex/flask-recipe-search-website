from flask import render_template
from flask.views import MethodView

from src.db_models import Recipe
from src.services import crud


class HomeView(MethodView):
    def get(self) -> str:
        recipes: list[Recipe] = crud.get_recipes()
        return render_template('index.html', recipes=recipes)
