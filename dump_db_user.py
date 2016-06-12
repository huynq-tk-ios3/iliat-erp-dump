from mlab import *
from users import User
import mongoengine
from util import *



if __name__ == "__main__":
    db = mongoengine.connect(db_name,
                             host=host, port=port, username=user_name, password=password)


    # user = User(user_name="android@hungdepzai.techkids.vn", password="123456")
    # user.save()

    # users = User.objects
    # for user in users:
    #     print(remove_dollar_sign(user.to_json()))
    #
    # admin_user = User.objects(user_name="admin")
    # for user in admin_user:
    #      print(remove_dollar_sign(user.to_json()))
    user = User(user_name = "admin", password="admin")
    user.save()
    db.close()
