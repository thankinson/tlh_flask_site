from flask import redirect, url_for, render_template, request
from application import db
from application.models.models import Users, UserAdmin
from application.forms.forms import UserRegistration, UserLogin, ChangePassword, RemoverAccount
from application import bcrypt
from flask_login import login_user, current_user, logout_user, login_required

class Userservice():
    def Adduser(form):
        print("Add user hit")
        print(form)
        hash_pw = bcrypt.generate_password_hash(form.password.data)
        user = Users(
            user_name = form.user_name.data,
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            user_email = form.user_email.data,
            password = hash_pw
        )
        print("user hit")
        print(user)
        db.session.add(user)
        addUserAdmin = UserAdmin(users=user)
        db.session.add(addUserAdmin)
        db.session.commit()
        print("Hurray Submitted")
            
class Loginservice():
    def is_logged_in(current_user):
        if current_user.is_authenticated:
            return redirect(url_for('index'))
    
    def log_in(logform):
        user = Users.query.filter_by(user_name=logform.user_name.data).first()
        if user and bcrypt.check_password_hash(user.password, logform.password.data):
            print("Login service if hit")
            print(user.user_name)
            user.remember_user = True
            login_user(user, remember=True)
    
    def logout():
        logout_user()
        return redirect(url_for('index'))

class DeleteService():
    def deleteUser():
        user = Users.query.filter_by(user_name=current_user.user_name).first()
        delete_role = UserAdmin.query.filter_by(user_id=user.id).first()
        db.session.delete(user)
        db.session.delete(delete_role)
        db.session.commit()
        logout_user()

class UpdateService():
    def updatePass(changeform):
        print("Update pass hit")
        user = Users.query.filter_by(user_name=current_user.user_name).first()
        if user and bcrypt.check_password_hash(user.password, changeform.password.data):
            if changeform.new_pass.data == changeform.confirm_new_pass.data:
                hash_pw = bcrypt.generate_password_hash(changeform.new_pass.data)
                user.password = hash_pw
                db.session.commit()

class SignUpPage():
    def SignUp():
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

class DashboardPage():
    def DashBoard():
        changeform = ChangePassword()
        removeform = RemoverAccount()
        if not current_user.is_authenticated:
            return redirect(url_for('index'))
        if changeform.validate_on_submit():
            if request.method == "POST":
                UpdateService.updatePass(changeform=changeform)
        elif removeform.validate_on_submit():
            if request.method == "POST":
                DeleteService.deleteUser()
                return redirect(url_for('index'))
        return render_template('dashboard.html', changeform=changeform, removeform=removeform)

class AdminPage():
    def checkAdmin():
        if current_user.is_authenticated:
            isAdmin = UserAdmin.query.filter_by(user_id=current_user.id).first()
            if current_user.id == isAdmin.user_id:
                if isAdmin.roles_id == 1:
                    isUser = db.session.query(Users, UserAdmin).join(UserAdmin).all()
                    return render_template('adminpage.html', users=isUser)                
                else:
                    return redirect(url_for('dashboard'))
        else: 
            return redirect(url_for('index'))

    def deleteUserById(id):
        delete_user = Users.query.filter_by(id=id).first()
        delete_role = UserAdmin.query.filter_by(user_id=id).first()
        db.session.delete(delete_user)
        db.session.delete(delete_role)
        db.session.commit()
        return redirect(url_for('admin'))
    
    def updateUserAminById(id):
        find_user = UserAdmin.query.filter_by(user_id=id).first()
        find_user.roles_id = 1
        db.session.commit()
        return redirect(url_for('admin'))