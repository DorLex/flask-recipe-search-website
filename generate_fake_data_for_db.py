from project.app import app
from fake_data_for_db.generate_data import save_data_to_db

if __name__ == '__main__':
    with app.app_context():
        save_data_to_db()

    print('---OK---')
