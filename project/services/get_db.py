from project.db_models import db, Recipes, Ingredients


def get_recipe(recipe_id):
    # recipe = Recipes.query.get(recipe_id)
    recipe = db.session.execute(db.select(Recipes).filter_by(id=recipe_id)).scalar()
    return recipe


def get_recipes():
    # recipes = Recipes.query.order_by(Recipes.id.desc()).limit(5)
    recipes = db.session.execute(
        db.select(Recipes).order_by(Recipes.id.desc()).limit(5)
    ).scalars()

    return recipes


def get_ingredients(json_data):
    # ingredients = Ingredients.query.filter(Ingredients.ingredient.ilike(f'%{json_data["ingredient"]}%')).all()
    ingredients = db.session.execute(
        db.select(Ingredients).filter(Ingredients.ingredient.ilike(f'%{json_data["ingredient"]}%'))
    ).scalars()

    return ingredients
