from flask import render_template
from flask.views import MethodView

from project.db_models import Recipes
from project.services import crud


class HomeView(MethodView):
    def get(self):
        recipes: list[Recipes] = crud.get_recipes()
        return render_template('index.html', recipes=recipes)
