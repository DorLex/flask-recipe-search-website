from flask_debugtoolbar import DebugToolbarExtension

from src.app import app

toolbar: DebugToolbarExtension = DebugToolbarExtension(app)
