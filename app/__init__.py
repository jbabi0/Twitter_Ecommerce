# import necessary files
from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config

# set application variables, app variable must be set first
app = Flask(__name__)


# set config variables for this application

app.config.from_object(Config)


bootstrap = Bootstrap(app)

# import routes

from app import routes
