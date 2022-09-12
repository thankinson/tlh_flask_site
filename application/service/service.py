import email
from urllib import request
from flask import redirect, url_for
from application import db
from application.models.models import Users
from application import bcrypt
from flask_login import login_user, current_user, logout_user, login_required


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

class Loginservice():
    def is_logged_in():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
    
    def log_in(form):
        print("Login service hit")

        user = Users.query.filter_by(user_name=form.user_name.data).first()
        print(user.user_name)
        print(user.password)

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            print("Login service if hit")

            login_user(user)
            print(user.user_name, ' Login_user')
            # next_page = request.args.get('index')
            # if next_page:
            #     return redirect(url_for(next_page))
            # else:
            #     return redirect('index')