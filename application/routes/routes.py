from flask import Flask, render_template
from application import app
from application.forms.forms import UserRegistration, UserLogin
from application.service.service import Userservice

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    message = ""
    form = UserRegistration()
    if form.validate_on_submit():
        try:
            Userservice.Adduser(form=form)
            message = "User added to database"
        except:
            message = "user already in db"

    return render_template('signup.html', form=form, message=message)


################################################################
####           functions that have been replaced            ####
    # if form.validate_on_submit():
    #     hash_pw = bcrypt.generate_password_hash(form.password.data)
    #     users = Users(
    #         user_name = form.user_name.data,
    #         first_name = form.first_name.data,
    #         last_name = form.last_name.data,
    #         user_email = form.user_email.data,
    #         password = hash_pw
    #     )

    #     db.session.add(users)
    #     db.session.commit()
    #     message = "User added to database"

    # return render_template('signup.html', form=form, message=message)