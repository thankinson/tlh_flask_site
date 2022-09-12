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
    Userservice.Adduser(form=form)

    # if form.validate_on_submit():
    #     try:
    #         Userservice.Adduser(form=form)
    #         message = "User added to database"
    #     except:
    #         message = "User Name or Email Already in use"

    return render_template('signup.html', form=form, message=message)