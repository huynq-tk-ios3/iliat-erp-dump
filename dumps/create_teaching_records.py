from models import classes
from utils import mlab
from models.teachingrecords import TeachingRecord
import random

mlab.connect()

instructors_data = {
    "items": [
        {
            "name": "Nguyen Son Vu",
            "code": "02004",
            "team": "ios",
            "image": "http://i.imgur.com/mSCSREI.jpg?1",
            "classes": [
                {
                    "code": "ios5",
                    "role": "inst"
                },
                {
                    "code": "ios5",
                    "role": "coach"
                },
                {
                    "code": "ios6",
                    "role": "inst"
                }
            ],
        },
        {
            "name": "Trinh Quang Dai",
            "code": "02005",
            "team": "ios",
            "image": "http://i.imgur.com/7qab6QK.jpg",
            "classes": [
                {
                    "code": "ci5",
                    "role": "coach"
                },
                {
                    "code": "ci5",
                    "role": "inst"
                },
                {
                    "code": "ios6",
                    "role": "coach"
                },
                {
                    "code": "ios6",
                    "role": "inst"
                },
                {
                    "code": "ios7",
                    "role": "inst"
                }
            ],
        },
        {
            "name": "Tran Duc Hung",
            "code": "01002",
            "team": "android",
            "image": "http://i.imgur.com/7qab6QK.jpg",
            "classes": [
                {
                    "code": "ci5",
                    "role": "inst"
                },
                {
                    "code": "android3",
                    "role": "coach"
                },
                {
                    "code": "android3",
                    "role": "inst"
                },
                {
                    "code": "android4",
                    "role": "inst"
                }
            ],
        },
        {
            "name": "Bui Xuan Canh",
            "code": "01002",
            "team": "android",
            "image": "http://i.imgur.com/7qab6QK.jpg",
            "classes": [
                {
                    "code": "android1",
                    "role": "inst"
                },
                {
                    "code": "android3",
                    "role": "inst"
                }
            ],
        },
        {
            "name": "Ta Hoang Minh",
            "code": "02003",
            "team": "ios",
            "image": "http://i.imgur.com/7qab6QK.jpg",
            "classes": [
                {
                    "code": "ios4",
                    "role": "inst"
                },
                {
                    "code": "ios5",
                    "role": "inst"
                }
            ],
        }
    ]
}

dates = [
   "2016-06-14",
   "2016-06-15",
   "2016-06-16",
   "2016-06-17",
   "2016-06-18",
   "2016-06-19"
]

users = [
    "vuns",
    "admin"
]

for record in TeachingRecord.objects():
    print("deleting object : {0}".format(record.to_json()))
    record.delete()

if len(TeachingRecord.objects()) == 0:
   for instructor_dict in instructors_data["items"]:
       code = instructor_dict["code"]
       num = random.randint(2, 4)
       for _ in range(num):
           date = random.choice(dates)
           class_role = random.choice(instructor_dict['classes'])
           user_name = random.choice(users)
           record = TeachingRecord(
               instructor_code = instructor_dict['code'],
               role_code = class_role['role'],
               class_code = class_role['code'],
               date = date,
               user_name = user_name
           )
           print(record.to_json())
           record.save()

mlab.disconnect()
