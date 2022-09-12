from application import db, login_manager

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(30), nullable=False, unique=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    user_email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)

    # def __repr__(self) -> str:
    #     return ''.join(['UserId: ', str(self.id), '\r\n',
    #     'Email: ', self.user_email], '\r\n'
    #     'Name: ', self.first_name, ' ', self.last_name,
    #     '\r\n'
    #     'User Name: ', self.user_name 
    #     )

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))
