import logging
from logging import INFO, Logger, getLogger
from random import randint

from sqlalchemy import Select

from src.app import app
from src.db_models import Ingredients, Recipes, db

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
            self._save_fake_data_to_db()

        logger.info('✅️ DB data generated successfully')

    def _save_fake_data_to_db(self) -> None:
        for recipes_num in range(1, 16):
            recipe: Recipes = self.create_recipe(recipes_num)
            self._save(recipe)

            used_numbers = set()
            for _ in range(5):
                ingredient_num: int = self.get_ingredient_num(used_numbers)

                ingredient: Ingredients = self.get_or_create_ingredient(ingredient_num)
                self._save(ingredient)

                recipe.ingredients.append(ingredient)

            db.session.commit()

    def _save(self, obj: db.Model) -> None:
        db.session.add(obj)
        db.session.flush()

    def create_recipe(self, recipes_num: int) -> Recipes:
        return Recipes(
            title=f'Рецепт {recipes_num}',
            description=f'описание рецепта {recipes_num} ' * 50,
        )

    def _get_ingredient(self, ingredient_num: int) -> Ingredients | None:
        query: Select = db.select(Ingredients).filter_by(title=f'ингредиент {ingredient_num}')
        ingredient: Ingredients | None = db.session.execute(query).scalar()

        return ingredient

    def _create_ingredient(self, ingredient_num: int) -> Ingredients:
        return Ingredients(
            title=f'ингредиент {ingredient_num}',
            weight=f'{ingredient_num}0 гр',
        )

    def get_or_create_ingredient(self, ingredient_num: int) -> Ingredients:
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
