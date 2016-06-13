from mongoengine import Document, StringField

class User(Document):
    user_name = StringField(max_length=50)
    password = StringField(max_length=30)
