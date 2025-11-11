from logging import Logger, getLogger

from fake_data_for_db.generate_data import save_fake_data_to_db
from src.app import app

logger: Logger = getLogger(__name__)
if __name__ == '__main__':
    with app.app_context():
        save_fake_data_to_db()

    logger.info('--- generate data successfully ---')
