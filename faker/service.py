import logging
from logging import INFO, Logger, getLogger
from random import randint

from sqlalchemy import Select

from src.app import app
from src.db_models import Ingredient, Recipe, db

logging.basicConfig(level=INFO)
logger: Logger = getLogger(__name__)


class Faker:
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
            recipe: Recipe = self.create_recipe(recipe_num)
            self._save(recipe)

            used_numbers = set()
            for _ in range(5):
                ingredient_num: int = self.get_ingredient_num(used_numbers)

                ingredient: Ingredient = self.get_or_create_ingredient(ingredient_num)
                self._save(ingredient)

                recipe.ingredients.append(ingredient)

            db.session.commit()

    def _save(self, obj: db.Model) -> None:
        db.session.add(obj)
        db.session.flush()

    def create_recipe(self, recipes_num: int) -> Recipe:
        return Recipe(
            title=f'Рецепт {recipes_num}',
            description=f'описание рецепта {recipes_num} ' * 50,
        )

    def _get_ingredient(self, ingredient_num: int) -> Ingredient | None:
        query: Select = db.select(Ingredient).filter_by(title=f'ингредиент {ingredient_num}')
        ingredient: Ingredient | None = db.session.execute(query).scalar()

        return ingredient

    def _create_ingredient(self, ingredient_num: int) -> Ingredient:
        return Ingredient(
            title=f'ингредиент {ingredient_num}',
            weight=f'{ingredient_num}0 гр',
        )

    def get_or_create_ingredient(self, ingredient_num: int) -> Ingredient:
        return self._get_ingredient(ingredient_num) or self._create_ingredient(ingredient_num)

    def _get_random_num(self) -> int:
        return randint(1, 10)

    def get_ingredient_num(self, used_numbers: set) -> int:
        while True:
            random_num: int = self._get_random_num()

            if random_num not in used_numbers:
                used_numbers.add(random_num)

                return random_num


if __name__ == '__main__':
    faker: Faker = Faker()
    faker.recreate_db_tables()
    faker.generate_data()
