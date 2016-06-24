from bson import ObjectId
from flask import Flask

import json
from flask import request, redirect
import mongoengine

from models.versions import Version
from models.users import User
from models.roles import Role
from models.classes import  Class
from models.teachingrecords import TeachingRecord

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
    return redirect('http://localhost:9696')

@app.route('/api/login', methods=['POST'])
def login():
    user_name = request.form['username'];
    password = request.form['password'];
    for user in User.objects(user_name=user_name):
        if(user.password == password):
            return json.dumps({"result_code":1, "result_message":"Login succeded"})
    return json.dumps({"result_code":0, "result_message":"Login failed"})




@app.route('/api/instructors')
def get_instructors():
    return json.dumps(
        instructors_dump
    )

@app.route('/api/classes')
def get_classes():
    return json.dumps(
        {
            "items": [cl.to_json() for cl in Class.objects]
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
@app.route('/api/instructor/add-teaching-record', methods=['POST'])
def add_instructor_record():
    print("add_instructor_record")
    instructor_code = request.form['code']
    class_ = request.form['class']
    role = request.form['role']
    date = request.form['date']
    # print("Sending result")
    return json.dumps({"result_code": 1, "result_message":"Record was added successfully",
                       "record_id": "409824590237840578"})

@app.route('/api/instructor/teaching-records', methods=['GET'])
def get_teaching_record_by_code():
    instructor_code = request.args['code']
    return json.dumps(
        {
            "items": [record.to_json() for record in TeachingRecord.objects(instructor_code = instructor_code)]
        }
    )

@app.route('/api/instructor/get-teaching-record', methods=['GET'])
def get_teaching_records():
    if "instructor_code" in request.args:
        return json.dumps(
            {
                "items": [record.to_json() for record in TeachingRecord.objects(
                    instructor_code = request.args["instructor_code"])]
            }
        )
    else:
        return json.dumps(
            {
                "items": [record.to_json() for record in TeachingRecord.objects]
            }
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
