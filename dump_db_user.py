from mlab import *
from users import User
import mongoengine
from util import *

if __name__ == "__main__":
    db = mongoengine.connect(db_name,
                             host=host, port=port, username=user_name, password=password)
    user = User(user_name = "admin", password="admin")
    user.save()
    db.close()
