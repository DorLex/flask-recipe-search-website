from decouple import config
from flask_debugtoolbar import DebugToolbarExtension

from project.app import app

DATABASE_USER = config('DATABASE_USER')
DATABASE_PASSWORD = config('DATABASE_PASSWORD')
DATABASE_HOST = config('DATABASE_HOST')
DATABASE_NAME = config('DATABASE_NAME')

SQLALCHEMY_DATABASE_URI = f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}'

app.debug = config('DEBUG', cast=bool)

app.config['SECRET_KEY'] = config('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

# для отображения sql запросов в flask debug toolbar
app.config['SQLALCHEMY_RECORD_QUERIES'] = config('SQLALCHEMY_RECORD_QUERIES', cast=bool)

toolbar = DebugToolbarExtension(app)
