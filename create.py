from application import db
from application.models.models import Users, UserAdmin, UserRoles
from application import bcrypt

# check_user = Users.query.filter_by(user_name='thankinson'.lower()).first()

# print(check_user.user_name)




db.drop_all()
db.create_all()
# add usr works
# hash_pw = bcrypt.generate_password_hash('password')
# AdminUser = Users(
#     user_name='thankinson',
#     first_name='tom',
#     last_name='hankinson',
#     user_email='tom@email.com',
#     password= hash_pw
#     )
# db.session.add(AdminUser)

# addAdmin = AdminTable(
#     user_name='thankinson',
#     first_name='tom',
#     last_name='hankinson'
#     )
# db.session.add(addAdmin)

# addUserAdmin = UserAdmin(users=AdminUser, admintable=addAdmin)
# db.session.add(addUserAdmin)

# db.session.commit()