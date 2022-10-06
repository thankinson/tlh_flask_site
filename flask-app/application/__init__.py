from flask import Flask
from os import environ
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from application.modules.csrf import csrf, CSRFError

app = Flask(__name__)

app.config['SECRET_KEY'] = 'bA5qzruPYLAyyx5QFNUVCg'
app.config['SECRET_KEY'] = 'bA5qzruPYLAyyx5QFNUVCg'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get("db_connection")

print(app.config['SQLALCHEMY_DATABASE_URI'])
db =SQLAlchemy(app)

bcrypt = Bcrypt(app)        
csrf.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

from application.routes import routes
from application.models import models