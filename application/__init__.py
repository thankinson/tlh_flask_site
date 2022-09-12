from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SECRET_KEY'] = 'bA5qzruPYLAyyx5QFNUVCg'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

db =SQLAlchemy(app)
bcrypt = Bcrypt(app)

from application.routes import routes
from application.models import models
