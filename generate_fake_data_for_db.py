from src.app import app
from fake_data_for_db.generate_data import save_fake_data_to_db

if __name__ == '__main__':
    with app.app_context():
        save_fake_data_to_db()

    print('--- generate data successfully ---')
