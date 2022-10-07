from flask import render_template
from application import db
from application.models.models import Users, UserAdmin
from application import bcrypt

class DbConnect():
    def createdatabase():
        DbConnect.create_db()
        return render_template('index.html')
        
    def create_db():
        # default password for all suers is password
        db.drop_all()
        db.create_all()
        hash_pw = bcrypt.generate_password_hash('password')
        AdminUser = Users(
            user_name='admin',
            first_name='admin',
            last_name='admin',
            user_email='admin@email.com',
            password= hash_pw
            )
        db.session.add(AdminUser)
        addUserAdmin = UserAdmin(
                            users=AdminUser,
                            roles_id= 1)
        db.session.add(addUserAdmin)
        db.session.commit()