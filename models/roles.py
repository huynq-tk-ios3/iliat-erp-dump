from mongoengine import Document, StringField

class Role(Document):
    code = StringField()
    title = StringField()
