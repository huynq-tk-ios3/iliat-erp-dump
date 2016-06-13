from mongoengine import Document, StringField, IntField

class Instructor(Document):
    name = StringField()
    code = StringField()
    team = StringField()
    image = StringField()
    classes = []
