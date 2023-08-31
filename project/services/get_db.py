from project.db_models import db, Recipes, Ingredients


def get_recipe_by_id(recipe_id):
    recipe = db.session.execute(db.select(Recipes).filter_by(id=recipe_id)).scalar()
    return recipe


def get_recipes():
    recipes = db.session.execute(
        db.select(Recipes).order_by(Recipes.id.desc()).limit(5)
    ).scalars()

    return recipes


def get_ingredients_ilike(ingredient):
    ingredients = db.session.execute(
        db.select(Ingredients).filter(Ingredients.ingredient.ilike(f'%{ingredient}%'))
    ).scalars()

    return ingredients
