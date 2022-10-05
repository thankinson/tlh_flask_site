from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from application.modules.csrf import csrf, CSRFError

app = Flask(__name__)

app.config['SECRET_KEY'] = 'bA5qzruPYLAyyx5QFNUVCg'
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@database:3306/finalproject'
db_user = "root"
db_pass = "password"
db_name = "finalproject"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@database:3306/finalproject'.format(db_user, db_pass, db_name)

db =SQLAlchemy(app)
bcrypt = Bcrypt(app)        
csrf.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

from application.routes import routes
from application.models import models