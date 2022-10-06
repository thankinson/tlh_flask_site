from application import db
from application.models.models import Users, UserAdmin
from application import bcrypt


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

# users
AdminUser = Users(
    user_name='jsmith',
    first_name='john',
    last_name='smith',
    user_email='jsmith@email.com',
    password= hash_pw
    )
db.session.add(AdminUser)

addUserAdmin = UserAdmin(
                    users=AdminUser)
db.session.add(addUserAdmin)

AdminUser = Users(
    user_name='ssmith',
    first_name='sarah',
    last_name='smith',
    user_email='ssmith@email.com',
    password= hash_pw
    )
db.session.add(AdminUser)

addUserAdmin = UserAdmin(
                    users=AdminUser)
db.session.add(addUserAdmin)

db.session.commit()