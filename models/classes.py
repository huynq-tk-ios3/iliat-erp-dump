from mongoengine import Document, StringField

class Class(Document):
    code = StringField()
    title = StringField()
