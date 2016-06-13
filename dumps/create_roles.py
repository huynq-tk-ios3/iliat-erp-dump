from models import classes
from utils import mlab
from models.roles import Role

mlab.connect()


if len(Role.objects()) == 0:
   Role(code = "inst", title = "Instructor").save()
   Role(code = "coach", title = "Coach").save()

mlab.disconnect()
