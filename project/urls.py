from project.app import app
from project.controllers.about import About
from project.controllers.home import HomeView
from project.controllers.live_search import LiveSearchIngredients
from project.controllers.recipes import RecipeDetails, SearchRecipes

urls = [
    app.add_url_rule('/', view_func=HomeView.as_view('home')),
    
    app.add_url_rule('/recipe/<int:recipe_id>', view_func=RecipeDetails.as_view('recipe_details')),
    app.add_url_rule('/search-recipes-by-ingredients', view_func=SearchRecipes.as_view('search_recipes')),
    app.add_url_rule('/live-search', view_func=LiveSearchIngredients.as_view('live_search_ingredients')),

    app.add_url_rule('/about', view_func=About.as_view('about')),
]
