# import necessary files
from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


# set appilication variables, app variables must be set first
app = Flask(__name__)

# set config variables for this appilication
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db) # migrate class needs to know which app and db instance to use
bootstrap = Bootstrap(app)
login = LoginManager(app)

# setting the @login_required function to send the user to the route 'login'
login.login_view = 'login'

# import routes
from app import routes
