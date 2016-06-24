from mongoengine import *
class TeachingRecord(Document):
    instructor_code = StringField()
    role_code = StringField()
    class_code = StringField()
    date = StringField()
    user_name = StringField()