from project.db_models import db, Recipes, Ingredients, Book


def _parse_search_elements(ingredients_str):
    search_elements_list = ingredients_str.split(',')
    return search_elements_list


def _get_recipes_id_by_ingredient(ingredient):
    recipes_id_select_obj = db.select(Recipes.id) \
        .join(Book, Book.recipe_id == Recipes.id) \
        .join(Ingredients, Book.ingredient_id == Ingredients.id) \
        .filter(Ingredients.ingredient.ilike(f'%{ingredient}%'))

    return recipes_id_select_obj


def _search_recipes_id_by_ingredients(search_elements):
    recipes_id_select_objs = []
    for ingredient in search_elements:
        recipes_id_select_objs.append(_get_recipes_id_by_ingredient(ingredient))

    return recipes_id_select_objs


def _intersect_queries(query_objs):
    intersect_query = db.intersect(*query_objs)
    return intersect_query


def _get_intersect_recipes_list(intersect_recipes_id_query):
    recipes_list = db.session.execute(
        db.select(Recipes).filter(Recipes.id.in_(intersect_recipes_id_query))
    ).scalars().all()

    return recipes_list


def get_recipes_by_ingredients(ingredients_str):
    search_ingredients_list = _parse_search_elements(ingredients_str)
    recipes_id_query_objs = _search_recipes_id_by_ingredients(search_ingredients_list)
    intersect_recipes_id_query = _intersect_queries(recipes_id_query_objs)
    recipes_list = _get_intersect_recipes_list(intersect_recipes_id_query)

    return recipes_list
