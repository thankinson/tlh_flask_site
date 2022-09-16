from flask import Flask, render_template, redirect, url_for, request
from application import app, csrf
from application.forms.forms import UserRegistration, UserLogin
from application.models.models import Users
from application.service.service import Userservice, Loginservice
from flask_login import current_user


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
@csrf.exempt
def register():
    # Loginservice.is_logged_in()  #### this is not yet working
    message = ""
    form = UserRegistration()
    logform = UserLogin()
    if form.validate_on_submit():
        if request.method == 'POST':
            try:
                Userservice.Adduser(form=form)
                message = "User added to database"
            except:
                message = "User Name or Email Already in use"
        
    elif logform.validate_on_submit():
        if request.method == 'POST':
            try:
                Loginservice.log_in(logform=logform)
                if current_user.is_authenticated:
                    return redirect(url_for('index'))
                else:
                    message = "User Name or Password Incorrect"
            except:
                message = "Fatel Error: The Admin Gods do not smile upon you"  

    return render_template('signup.html', form=form, logform=logform, message=message)