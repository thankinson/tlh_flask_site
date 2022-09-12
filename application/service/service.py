from application import db
from application.models.models import Users
from application import bcrypt

class Userservice():
        def Adduser(form):
            hash_pw = bcrypt.generate_password_hash(form.password.data)
            users = Users(
                user_name = form.user_name.data,
                first_name = form.first_name.data,
                last_name = form.last_name.data,
                user_email = form.user_email.data,
                password = hash_pw
            )

            db.session.add(users)
            db.session.commit()
            