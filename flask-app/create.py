from application import db
from application.models.models import Users, UserAdmin, UserRoles
from application import bcrypt

# check_user = Users.query.filter_by(user_name='thankinson'.lower()).first()

# print(check_user.user_name)

db.drop_all()
db.create_all()
# add usr works
# admin user
hash_pw = bcrypt.generate_password_hash('password')
AdminUser = Users(
    user_name='thankinson',
    first_name='tom',
    last_name='hankinson',
    user_email='tom@email.com',
    password= hash_pw
    )
db.session.add(AdminUser)

AdminRole = UserRoles(
    roles = 'admin',
    readAllowed = True,
    writeAllowed = True
    )
db.session.add(AdminRole)

addUserAdmin = UserAdmin(users=AdminUser, UserRoles=AdminRole)
db.session.add(addUserAdmin)

# users
hash_pw = bcrypt.generate_password_hash('password')
AdminUser = Users(
    user_name='jsmith',
    first_name='john',
    last_name='smith',
    user_email='john@email.com',
    password= hash_pw
    )
db.session.add(AdminUser)

AdminRole = UserRoles(
    roles = 'user',
    readAllowed = True,
    writeAllowed = False
    )
db.session.add(AdminRole)

addUserAdmin = UserAdmin(users=AdminUser, UserRoles=AdminRole)
db.session.add(addUserAdmin)

hash_pw = bcrypt.generate_password_hash('password')
AdminUser = Users(
    user_name='sboyd',
    first_name='sarah',
    last_name='boyd',
    user_email='sarah@email.com',
    password= hash_pw
    )
db.session.add(AdminUser)

addUserAdmin = UserAdmin(users=AdminUser, UserRoles=AdminRole)
db.session.add(addUserAdmin)

db.session.commit()