from mongoengine import *

class Version(Document):
    value = ListField(IntField())
