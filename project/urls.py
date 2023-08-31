from project import app
from project import controllers

# class Router:
#     app.add_url_rule('/', view_func=Handler.index, methods=['POST', 'GET'])
#     app.add_url_rule('/search/<ing>', view_func=Handler.search, methods=['POST', 'GET'])
#     app.add_url_rule('/<recipe_id>', view_func=Handler.recipe_details, methods=['POST', 'GET'])
#     app.add_url_rule('/about', view_func=Handler.about, methods=['POST', 'GET'])
#     app.add_url_rule('/live-search', view_func=Handler.live_search, methods=['POST', 'GET'])


urls = [
    app.add_url_rule('/', view_func=controllers.HomeView.as_view('home')),
    app.add_url_rule('/recipe/<int:recipe_id>', view_func=controllers.RecipeDetails.as_view('recipe_details')),
    app.add_url_rule('/about', view_func=controllers.About.as_view('about')),
    app.add_url_rule('/search-recipes/<ingredients>', view_func=controllers.SearchRecipes.as_view('search_recipes')),
    app.add_url_rule('/live-search', view_func=controllers.LiveSearchIngredients.as_view('live_search_ingredients')),
]
