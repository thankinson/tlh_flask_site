from application import db, login_manager
from flask_login import UserMixin

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(30), nullable=False, unique=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    user_email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    # remember_user = db.Column(db.Boolean, default=False)
    admin_id = db.relationship('UserAdmin', backref='users')

    # def is_active(self):
    #     return True
    
    # def get_id(self):
    #     # return self.user_email
    #     return self.id
    
    # def is_authenticated(self):
    #     return self.remember_user

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

class UserAdmin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
    roles_id = db.Column(db.Integer, default=2)   