from mongoengine import Document, StringField, IntField, ListField

class Instructor(Document):
    name = StringField()
    code = StringField()
    team = StringField()
    image = StringField()
    classes = ListField(ClassRole)

class ClassRole(Document):
    class_code = StringField()
    role_code = StringField()