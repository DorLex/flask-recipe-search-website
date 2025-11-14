from flask import render_template
from flask.views import MethodView


class About(MethodView):
    def get(self) -> str:
        return render_template('about.html', title='О сайте')
