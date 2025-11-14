from src.app import app
from src.controllers.about import About
from src.controllers.home import HomeView
from src.controllers.live_search import IngredientLiveSearchView
from src.controllers.recipe import RecipeView
from src.controllers.recipe_search import RecipeSearchView

urls: list = [
    app.add_url_rule('/', view_func=HomeView.as_view('home')),
    app.add_url_rule('/recipes/<int:recipe_id>', view_func=RecipeView.as_view('recipe_details')),
    app.add_url_rule('/recipe-search/by-ingredients', view_func=RecipeSearchView.as_view('recipe_search')),
    app.add_url_rule('/ingredient-live-search', view_func=IngredientLiveSearchView.as_view('ingredient_live_search')),
    app.add_url_rule('/about', view_func=About.as_view('about')),
]
