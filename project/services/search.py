from project.db_models import db, Recipes, Ingredients, Book


def _parse_search_elements(ingredients_str):
    search_elements_list = ingredients_str.split(',')
    return search_elements_list


def _search_recipes_id_by_ingredients(search_elements):
    recipes_id_query_objs = []  # list[query,] query() -> [(1,), (2,),]   (query рецептов на каждый ингредиент)
    for ingredient in search_elements:
        recipe_ids_select_obj = db.select(Recipes.id) \
            .join(Book, Book.recipe_id == Recipes.id) \
            .join(Ingredients, Book.ingredient_id == Ingredients.id) \
            .filter(Ingredients.ingredient.ilike(f'%{ingredient}%'))

        recipes_id_query_objs.append(recipe_ids_select_obj)

    return recipes_id_query_objs


def _intersect_queries(query_objs):
    result = db.intersect(*query_objs)
    return result


def _get_intersect_recipes_list(intersect_recipes_id_query):
    recipes_list = db.session.execute(
        db.select(Recipes).filter(Recipes.id.in_(intersect_recipes_id_query))
    ).scalars().all()

    return recipes_list


def get_recipes_by_ingredients(ingredients_str):
    search_ingredients_list = _parse_search_elements(ingredients_str)
    recipes_id_query_objs = _search_recipes_id_by_ingredients(search_ingredients_list)
    intersect_recipes_id_query = _intersect_queries(recipes_id_query_objs)
    recipes_list = _get_intersect_recipes_list(intersect_recipes_id_query)  # этот запрос можно убрать

    return recipes_list
