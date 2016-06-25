from models import classes
from utils import mlab
from models.roles import Role

mlab.connect()

for role in Role.objects():
   role.delete()

if len(Role.objects()) == 0:
   Role(code = "inst", title = "Instructor").save()
   Role(code = "coach", title = "Coach").save()

mlab.disconnect()
