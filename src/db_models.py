from flask_sqlalchemy import SQLAlchemy

from src.app import app

db = SQLAlchemy(app)

recipes_ingredients = db.Table(
    'recipes_ingredients',
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipes.recipe_id'), primary_key=True),
    db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredients.ingredient_id'), primary_key=True),
)


class Recipes(db.Model):
    recipe_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)

    ingredients = db.relationship(
        'Ingredients',
        secondary=recipes_ingredients,
        back_populates='recipes',
        lazy='joined',
    )

    def __repr__(self):
        return f'<{self.title}>'


class Ingredients(db.Model):
    ingredient_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    weight = db.Column(db.String(20), nullable=False)

    recipes = db.relationship(
        'Recipes',
        secondary=recipes_ingredients,
        back_populates='ingredients',
        lazy='joined',
    )

    def __repr__(self):
        return f'<{self.ingredient}>'
