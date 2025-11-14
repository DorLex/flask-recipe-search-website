from sqlalchemy import Table

from src.core.database import db

recipes_ingredients: Table = db.Table(
    'recipes_ingredients',
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id'), primary_key=True),
    db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredient.id'), primary_key=True),
)


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)

    ingredients = db.relationship(
        'Ingredient',
        secondary=recipes_ingredients,
        back_populates='recipes',
        lazy='joined',
    )

    def __repr__(self) -> str:
        return f'<Recipe:[{self.id}] "{self.title}">'


class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    weight = db.Column(db.String(20), nullable=False)

    recipes = db.relationship(
        'Recipe',
        secondary=recipes_ingredients,
        back_populates='ingredients',
        lazy='joined',
    )

    def __repr__(self) -> str:
        return f'<Ingredient:[{self.id}] "{self.title}">'
