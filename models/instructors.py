from mongoengine import Document, StringField, IntField

# {
#     "name" : "Nguyen Son Vu",
#     "code" : "02004",
#     "team" : "iOS",
#     "image" : "http://i.imgur.com/mSCSREI.jpg?1",
#     "classes" : [
#         {
#             "code" : "ios5",
#             "role" : ["coach", "inst"]
#         },
#         {
#             "code" : "ios6",
#             "role" : ["inst"]
#         }
#     ],
# }

class Instructor(Document):
    name = StringField()
    code = StringField()
    team = StringField()
    image = StringField()
    classes = []
