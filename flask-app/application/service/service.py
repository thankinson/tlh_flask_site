from flask import redirect, url_for, render_template
from application import db
from application.models.models import Users, UserAdmin
from application import bcrypt
from flask_login import login_user, current_user, logout_user, login_required


class Userservice():
        def Adduser(form):
            hash_pw = bcrypt.generate_password_hash(form.password.data)
            user = Users(
                user_name = form.user_name.data,
                first_name = form.first_name.data,
                last_name = form.last_name.data,
                user_email = form.user_email.data,
                password = hash_pw
            )
            db.session.add(user)
            addUserAdmin = UserAdmin(users=user)
            db.session.add(addUserAdmin)
            db.session.commit()
            
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

class DeleteService():
    def deleteUser():
        user = Users.query.filter_by(user_name=current_user.user_name).first()
        db.session.delete(user)
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

class AdminPage():
    def checkAdmin():
        if current_user.is_authenticated:
            isAdmin = UserAdmin.query.filter_by(user_id=current_user.id).first()
            if current_user.id == isAdmin.user_id:
                if isAdmin.roles_id == 1:
                    isUserRole = UserAdmin.query.all()
                    isUser = Users.query.all()
                    return render_template('adminpage.html', users=isUser, role=isUserRole)                
                else:
                    return redirect(url_for('dashboard'))
        else: 
            return redirect(url_for('index'))

    def deleteUserById(id):
        delete_user = Users.query.filter_by(id=id).first()
        db.session.delete(delete_user)
        db.session.commit()
        return redirect(url_for('admin'))




