from application import db
from application.models.models import Users

# check_user = Users.query.filter_by(user_name='thankinson'.lower()).first()

# print(check_user.user_name)

db.drop_all()
db.create_all()