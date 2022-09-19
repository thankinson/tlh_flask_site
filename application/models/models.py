from application import db, login_manager
from flask_login import UserMixin

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(30), nullable=False, unique=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    user_email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    remember_user = db.Column(db.Boolean, default=False)
    admin_id = db.relationship('UserAdmin', backref='users')

    
    # def __repr__(self) -> str:
    #     return ''.join(['UserId: ', str(self.id), '\r\n',
    #     'Email: ', self.user_email], '\r\n'
    #     'Name: ', self.first_name, ' ', self.last_name,
    #     '\r\n'
    #     'User Name: ', self.user_name 
    #     )

    def is_active(self):
        return True
    
    def get_id(self):
        # return self.user_email
        return self.id
    
    def is_authenticated(self):
        return self.remember_user

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

# class AdminTable(db.Model):
#     __tablename__ = 'admin_table'

#     id = db.Column(db.Integer, primary_key=True)
#     user_name = db.Column(db.String(30), nullable=False, unique=True)
#     first_name = db.Column(db.String(30), nullable=False)
#     last_name = db.Column(db.String(30), nullable=False)
#     user_id = db.relationship('UserAdmin', backref='admin_table')

class UserRoles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roles = db.Column(db.String(30), nullable=False)
    user_id = db.relationship('UserAdmin', backref='userroles')

class UserAdmin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
    roles_id = db.Column('roles_id', db.Integer, db.ForeignKey('userroles.id'))

    # admin_id = db.Column('admin_id', db.Integer, db.ForeignKey('admin_table.id'))