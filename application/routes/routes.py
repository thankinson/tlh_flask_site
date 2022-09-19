from flask import Flask, render_template, redirect, url_for, request
from application import app, csrf
from application.forms.forms import UserRegistration, UserLogin, ChangePassword, RemoverAccount
from application.service.service import Userservice, Loginservice, DeleteService, UpdateService
from flask_login import current_user, logout_user, login_required


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

# Sign up and login page. 
# Click the login tab above the signup window to switch forms and the same to switch back.
@app.route('/register', methods=['GET', 'POST'])
@csrf.exempt
def register():
    message = ""
    logmessage = ""
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
                    return redirect(url_for('dashboard'))
                else:
                    logmessage = "User Name or Password Incorrect"
            except:
                logmessage = "Fatel Error: The Admin Gods do not smile upon you"  

    return render_template('signup.html', form=form, logform=logform, message=message, logmessage=logmessage)

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    changeform = ChangePassword()
    removeform = RemoverAccount()
    message = ""
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if changeform.validate_on_submit():
        if request.method == "POST":
            UpdateService.updatePass(changeform=changeform)
    elif removeform.validate_on_submit():
        try:
            if request.method == "POST":
                DeleteService.deleteUser()
                message = "Succesfuly removed user"
                return redirect(url_for('index'))
        except:
            message = "Delete Failed"
  

    return render_template('dashboard.html', changeform=changeform, removeform=removeform)


# logout function
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
