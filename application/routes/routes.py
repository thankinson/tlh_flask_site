from flask import Flask, render_template
from application import app
from application.forms.forms import UserRegistration, UserLogin
from application.service.service import Userservice, Loginservice

@app.route('/')
@app.route('/home')
def index():
    Loginservice.is_logged_in()
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Loginservice.is_logged_in()
    message = ""
    form = UserRegistration()
    if form.validate_on_submit():
        try:
            Userservice.Adduser(form=form)
            message = "User added to database"
        except:
            message = "User Name or Email Already in use"

    return render_template('signup.html', form=form, message=message)


@app.route('/login', methods=['GET', 'POST'])
def login():
    print("Login page hit")
    message = ""
    Loginservice.is_logged_in()
    form = UserLogin()
    if form.validate_on_submit():
        try:
            print("Login page if hit")
            Loginservice.log_in(form=form)
            message = "Logged in"
        except:
            message = "User Name or Password Incorrect"  
    return render_template('login.html', form=form, message=message)