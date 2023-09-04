from flask_sqlalchemy import SQLAlchemy

from project.app import app

db = SQLAlchemy(app)


class RelationshipTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'))
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.id'))
    quantity_id = db.Column(db.Integer, db.ForeignKey('quantity.id'))

    def __repr__(self):
        return f'<Таблица связей>'


class Recipes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)

    relationship = db.relationship('RelationshipTable', backref='recipe')

    def __repr__(self):
        return f'<{self.title}>'


class Ingredients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredient = db.Column(db.Text, nullable=False)

    relationship = db.relationship('RelationshipTable', backref='ingredient')

    def __repr__(self):
        return f'<{self.ingredient}>'


class Quantity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Text, nullable=False)

    relationship = db.relationship('RelationshipTable', backref='quantity')

    def __repr__(self):
        return f'<{self.quantity}>'
