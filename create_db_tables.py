from src.db_models import db
from src.app import app

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()

    print('--- create tables successfully ---')
