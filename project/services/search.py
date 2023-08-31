from project.db_models import db, Recipes, Ingredients, Book


def get_search_elements(q):
    # search_elements = [x.strip() for x in q.split(',')]
    search_elements = q.strip().split(',')
    return search_elements


def search_for_recipe_matches(intersect_recipes_id_query):
    recipes_list = db.session.execute(
        db.select(Recipes).filter(Recipes.id.in_(intersect_recipes_id_query))
    ).scalars().all()

    return recipes_list


def intersect_recipes_id(query_objs):
    result = db.intersect(*query_objs)
    return result


def search_recipes_id_by_ingredients(search_elements):
    query_objs = []  # list[query,] query() -> [(1,), (2,),]   (query рецептов на каждый ингредиент)
    for ingredient in search_elements:
        recipe_ids_select_obj = db.select(Recipes.id) \
            .join(Book, Book.recipe_id == Recipes.id) \
            .join(Ingredients, Book.ingredient_id == Ingredients.id) \
            .filter(Ingredients.ingredient.ilike(f'%{ingredient}%'))

        query_objs.append(recipe_ids_select_obj)

    return query_objs


def get_recipes_list(ingredients):
    search_elements = get_search_elements(ingredients)
    query_objs = search_recipes_id_by_ingredients(search_elements)
    intersect_recipes_id_query = intersect_recipes_id(query_objs)
    recipes = search_for_recipe_matches(intersect_recipes_id_query)

    return recipes
