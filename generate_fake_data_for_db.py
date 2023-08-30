from project.create_app import app
from fake_data_for_db.write_fake_data_to_db import save_to_db

if __name__ == '__main__':
    with app.app_context():
        save_to_db()

    print('---OK---')
