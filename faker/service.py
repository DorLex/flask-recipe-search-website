import logging
from logging import INFO, Logger, getLogger
from random import randint

from sqlalchemy import Select

from src.app import app
from src.models import Ingredient, Recipe, db

logging.basicConfig(level=INFO)
logger: Logger = getLogger(__name__)


class Faker:
    def __init__(self) -> None:
        self.used_recipe_numbers: set[int] = set()

    def recreate_db_tables(self) -> None:
        with app.app_context():
            db.drop_all()
            db.create_all()

        logger.info('✅️ DB tables created successfully')

    def generate_data(self) -> None:
        with app.app_context():
            self._generate_data()

        logger.info('✅️ DB data generated successfully')

    def _generate_data(self) -> None:
        for recipe_num in range(1, 16):
            recipe: Recipe = self._create_recipe(recipe_num)

            for _ in range(5):
                ingredient_num: int = self._get_unique_ingredient_num()
                ingredient: Ingredient = self._get_or_create_ingredient(ingredient_num)
                recipe.ingredients.append(ingredient)

            db.session.commit()
            self.used_recipe_numbers = set()

    def _save(self, obj: db.Model) -> None:
        db.session.add(obj)
        db.session.flush()

    def _create_recipe(self, recipes_num: int) -> Recipe:
        recipe: Recipe = Recipe(
            title=f'Рецепт {recipes_num}',
            description=f'описание рецепта {recipes_num} ' * 50,
        )
        self._save(recipe)
        return recipe

    def _get_or_create_ingredient(self, ingredient_num: int) -> Ingredient:
        return self._get_ingredient(ingredient_num) or self._create_ingredient(ingredient_num)

    def _get_ingredient(self, ingredient_num: int) -> Ingredient | None:
        query: Select = db.select(Ingredient).where(Ingredient.title == f'ингредиент {ingredient_num}')
        ingredient: Ingredient | None = db.session.execute(query).scalar()

        return ingredient

    def _create_ingredient(self, ingredient_num: int) -> Ingredient:
        ingredient: Ingredient = Ingredient(
            title=f'ингредиент {ingredient_num}',
            weight=f'{ingredient_num}0 гр',
        )
        self._save(ingredient)
        return ingredient

    def _get_unique_ingredient_num(self) -> int:
        while True:
            random_num: int = randint(1, 10)

            if random_num not in self.used_recipe_numbers:
                self.used_recipe_numbers.add(random_num)
                return random_num


if __name__ == '__main__':
    faker: Faker = Faker()
    faker.recreate_db_tables()
    faker.generate_data()
