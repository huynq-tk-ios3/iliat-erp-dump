from utils import mlab
from models.instructors import *


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
                    "code": "ci54",
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

mlab.disconnect()