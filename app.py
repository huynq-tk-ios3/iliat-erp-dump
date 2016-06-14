from bson import ObjectId
from flask import Flask

import json
from flask import request, redirect
import mongoengine

from models.versions import Version
from models.users import User
from models.roles import Role

from mlab import  *

mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

app = Flask(__name__)

instructors_dump = {
        "items" : [
            {
                "name" : "Nguyen Son Vu",
                "code" : "02004",
                "team" : "ios",
                "image" : "http://i.imgur.com/mSCSREI.jpg?1",
                "classes" : [
                    {
                        "code" : "ios5",
                        "role" : "inst"
                    },
                    {
                        "code" : "ios5",
                        "role" : "coach"
                    },
                    {
                        "code" : "ios6",
                        "role" : "inst"
                    }
                ],
            },
            {
                "name" : "Trinh Quang Dai",
                "code" : "02005",
                "team" : "ios",
                "image" : "http://i.imgur.com/7qab6QK.jpg",
                "classes" : [
                    {
                        "code" : "ci5",
                        "role" : "coach"
                    },
                    {
                        "code": "ci5",
                        "role": "inst"
                    },
                    {
                        "code" : "ios6",
                        "role" : "coach"
                    },
                    {
                        "code" : "ios6",
                        "role" : "inst"
                    },
                    {
                        "code" : "ios7",
                        "role" : "inst"
                    }
                ],
            },
            {
                "name" : "Tran Duc Hung",
                "code" : "01002",
                "team" : "android",
                "image" : "http://i.imgur.com/7qab6QK.jpg",
                "classes" : [
                    {
                        "code" : "ci54",
                        "role" : "inst"
                    },
                    {
                        "code" : "android3",
                        "role" : "coach"
                    },
                    {
                        "code" : "android3",
                        "role" : "inst"
                    },
                    {
                        "code" : "android4",
                        "role" : "inst"
                    }
                ],
            },
            {
                "name" : "Bui Xuan Canh",
                "code" : "01002",
                "team" : "android",
                "image" : "http://i.imgur.com/7qab6QK.jpg",
                "classes" : [
                    {
                        "code" : "android1",
                        "role" : "inst"
                    },
                    {
                        "code" : "android3",
                        "role" : "inst"
                    }
                ],
            },
            {
                "name" : "Ta Hoang Minh",
                "code" : "02003",
                "team" : "ios",
                "image" : "http://i.imgur.com/7qab6QK.jpg",
                "classes" : [
                    {
                        "code" : "ios4",
                        "role" : "inst"
                    },
                    {
                        "code" : "ios5",
                        "role" : "inst"
                    }
                ],
            }
        ]
}

def remove_dollar_sign(s):
    OLD_OID = "$oid"
    NEW_OID = "oid"
    return s.replace(OLD_OID, NEW_OID)

@app.route('/')
def home_page():
    return redirect('http://techkids.vn/')

@app.route('/api/login', methods=['POST'])
def login():
    user_name = request.form['username'];
    password = request.form['password'];
    for user in User.objects(user_name=user_name):
        if(user.password == password):
            return json.dumps({"login_status":1, "login_message":"Login succeded"})
    return json.dumps({"login_status":0, "login_message":"Login failed"})
#                     "small": "http://imgur.com/E3zFiyK",
#                     "large": "http://imgur.com/a/GyUUC"



@app.route('/api/instructors')
def get_instructors():
    return json.dumps(
        instructors_dump
    )

@app.route('/api/classes')
def get_classes():
    return json.dumps (
        {
            "items" : [
            {
                "code" : "ios4",
                "title": "iOS4"
            },
            {
                "code" : "android5",
                "title" : "Android 5"
            },
            {
                "code" : "ci5",
                "title" : "Code intensive 5"
            },
            {
                "code" : "ios6",
                "title" : "IOS 6"
            },
            {
                "code" : "ios7",
                "title" : "IOS 7"
            }
            ]
        }
    )

@app.route('/api/roles')
def get_roles():
    return json.dumps (
        {
            "items" : [role.to_json() for role in Role.objects]
        }
    )
@app.route('/api/instructor')
def get_instructor():
    instructor_code = request.args.get("code")
    ret_list = []
    for instructor in instructors_dump["items"]:
        if instructor["code"] == instructor_code:
            ret_list.append(instructor)
    return json.dumps(
        ret_list
    )

@app.route('/api/test-deploy')
def test_deploy():
    return "deploy 0.0.1"

@app.route('/api/version')
def get_gmat_version():
    version = Version.objects[0]
    return remove_dollar_sign(str(version.to_json()))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9696)
