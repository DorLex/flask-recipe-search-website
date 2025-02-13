from flask import render_template
from flask.views import MethodView

from project.services import crud


class HomeView(MethodView):
    def get(self):
        recipes = crud.get_recipes()
        return render_template('index.html', recipes=recipes)
