from flask import Flask, render_template
from application import app, db
from application.forms.forms import UserRegistration, UserLogin
from application.models.models import Users
from application import bcrypt

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    message = ""
    form = UserRegistration()

    # ######## you need to fix this later. you are trying to check the db before you have sent the user infor or something like that
    if form.validate_on_submit():
        # print("submit hit")
        # check_user = Users.query.filter_by(user_name=form.user_name.lower()).first()
        # check_email = Users.query.filter_by(user_email=form.user_email.lower()).first()
        # print(check_user)
        # print(check_email)
        # if check_email.user_email == form.user_email.lower() or check_user.user_name == form.user_name.lower():
        #     message = "Account already exists"
        #     print("already in db")
        # else:
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
        message = "User added to database"

    return render_template('signup.html', form=form, message=message)
