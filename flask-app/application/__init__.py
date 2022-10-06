from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from application.modules.csrf import csrf, CSRFError
import pymysql

app = Flask(__name__)

app.config['SECRET_KEY'] = 'bA5qzruPYLAyyx5QFNUVCg'
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

# dbconnect = 'mysql+pymysql://root:password@database:3306/finalproject'

dbconnect = pymysql.connect(
    host='database',
    user='root',
    passwd='password',
    db='finalproject'
    )

app.config['SQLALCHEMY_DATABASE_URI'] = dbconnect
db =SQLAlchemy(app)

bcrypt = Bcrypt(app)        
csrf.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

from application.routes import routes
from application.models import models