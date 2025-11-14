from flask_sqlalchemy import SQLAlchemy

from src.app import app

db: SQLAlchemy = SQLAlchemy(app)
