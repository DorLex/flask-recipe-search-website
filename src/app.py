from flask import Flask

from src.core.settings import config

app: Flask = Flask(__name__)

app.debug = config.debug
app.config['SECRET_KEY'] = config.secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = config.postgresql_url

# для отображения SQL-запросов в flask-debug-toolbar
app.config['SQLALCHEMY_RECORD_QUERIES'] = config.sqlalchemy_record_queries
