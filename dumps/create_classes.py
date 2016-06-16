from utils import mlab
from models.classes import Class
mlab.connect()

if len(Class.objects) == 0:
    Class(code="ios4", title="iOS 4").save()
    Class(code="android3", title="Android 3").save()
    Class(code="ci5", title="Code Intensive 5").save()
    Class(code="ios5", title="iOS 5").save()

if len(Class.objects) < 5:
    Class(code="android5", title="Android 5").save()
    Class(code="ios6", title="iOS 6").save()
    Class(code="ios7", title="iOS 7").save()


mlab.disconnect()
