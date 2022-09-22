from application import db
from application.models.models import Users, UserAdmin, UserRoles
from application import bcrypt

# check_user = Users.query.filter_by(user_name='thankinson'.lower()).first()

# print(check_user.user_name)

db.drop_all()
db.create_all()
# add usr works
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
    roles = 'admin'
    )
db.session.add(AdminRole)

addUserAdmin = UserAdmin(users=AdminUser, UserRoles=AdminRole)
db.session.add(addUserAdmin)


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
    roles = 'user'
    )
db.session.add(AdminRole)

addUserAdmin = UserAdmin(users=AdminUser, UserRoles=AdminRole)
db.session.add(addUserAdmin)

db.session.commit()