from flask import Flask, render_template
from application import app, csrf
from application.service.service import Loginservice, SignUpPage, DashboardPage, AdminPage, DbConnect

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

# this is where you sign up or login
@app.route('/register', methods=['GET', 'POST'])
@csrf.exempt
def register():
    print("sign up hit")
    return SignUpPage.SignUp()

# dashboard any user has access to this
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return DashboardPage.DashBoard()

# logout function
@app.route('/logout')
def logout():
    return Loginservice.logout()

# admin only features
@app.route('/admin')
def admin():
    return AdminPage.checkAdmin()

@app.route('/delete/<int:id>')
def deleteuser(id):
    return AdminPage.deleteUserById(id=id)

@app.route('/updateuser/<int:id>')
def updateuser(id):
    return AdminPage.updateUserAminById(id=id)

@app.route('/createdb')
def createdatabase():
    return DbConnect.createdatabase()