from utils import mlab
from models.instructors import Instructor


mlab.connect()

if len(Instructor.objects) == 0:
    Instructor(name="Bui Xuan Canh", code="TEC001002", team="android", imgUrl="http://i.imgur.com/7qab6QK.jpg").save()

mlab.disconnect()