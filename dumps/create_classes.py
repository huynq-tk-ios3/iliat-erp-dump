from utils import mlab
from models.classes import Class
mlab.connect()

for obj in Class.objects():
    print("Deleting {0}".format(obj.code))
    obj.delete()

if len(Class.objects()) == 0:
    Class(code="ios4", title="iOS 4").save()
    Class(code="android3", title="Android 3").save()
    Class(code="ci5", title="Code Intensive 5").save()
    Class(code="ios5", title="iOS 5").save()
    Class(code="android5", title="Android 5").save()
    Class(code="ios6", title="iOS 6").save()
    Class(code="ios7", title="iOS 7").save()
    Class(code="android1", title="Android 1").save()

mlab.disconnect()
