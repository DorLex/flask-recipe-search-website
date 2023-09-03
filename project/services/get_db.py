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
    ingredients_list = db.session.execute(
        db.select(Ingredients.ingredient).filter(Ingredients.ingredient.ilike(f'%{ingredient}%'))
    ).scalars().all()

    return ingredients_list
