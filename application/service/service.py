from application import db
from application.models.models import Users
from application import bcrypt

class Userservice():
        def Adduser(form):
            # message = ""
            hash_pw = bcrypt.generate_password_hash(form.password.data)
            if form.validate_on_submit():
                try:
                    users = Users(
                        user_name = form.user_name.data,
                        first_name = form.first_name.data,
                        last_name = form.last_name.data,
                        user_email = form.user_email.data,
                        password = hash_pw
                    )

                    db.session.add(users)
                    db.session.commit()
                    return "User added to database"

                except:
                    return "User Name or Email Already in use"