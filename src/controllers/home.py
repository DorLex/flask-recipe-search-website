from flask import render_template
from flask.views import MethodView

from src.db_models import Recipes
from src.services import crud


class HomeView(MethodView):
    def get(self) -> str:
        recipes: list[Recipes] = crud.get_recipes()
        return render_template('index.html', recipes=recipes)
