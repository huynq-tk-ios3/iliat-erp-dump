from bson import ObjectId
from flask import Flask

from questions import Question, QuestionCollection
from versions import Version
from question_packs import QuestionPack, QuestionPackCollection
from users import User
import json
from flask import request
import mongoengine



from mlab import  *

mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

app = Flask(__name__)

def remove_dollar_sign(s):
    OLD_OID = "$oid"
    NEW_OID = "oid"
    return s.replace(OLD_OID, NEW_OID)

@app.route('/')
def home_page():
    return redirect('http://techkids.vn/')

@app.route('/api/login', methods=['POST'])
def gmat_login():
    user_name = request.form['username'];
    password = request.form['password'];
    for user in User.objects(user_name=user_name):
        if(user.password == password):
            return json.dumps({"login_status":1, "login_message":"Login Success"})
    return json.dumps({"login_status":0, "login_message":"Login Failed"})
#                     "small": "http://imgur.com/E3zFiyK",
#                     "large": "http://imgur.com/a/GyUUC"

instructors_dump = {
        "items" : [
            {
                "name" : "Nguyen Son Vu",
                "code" : "02004",
                "team" : "iOS",
                "image" : "http://i.imgur.com/mSCSREI.jpg?1",
                "classes" : [
                    {
                        "code" : "iOS5",
                        "role" : ["coach", "instructor"]
                    },
                    {
                        "code" : "iOS6",
                        "role" : ["instructor"]
                    }
                ],
            },
            {
                "name" : "Trinh Quang Dai",
                "code" : "02005",
                "team" : "iOS",
                "image" : "http://i.imgur.com/7qab6QK.jpg",
                "classes" : [
                    {
                        "code" : "CI5",
                        "role" : ["coach", "instructor"]
                    },
                    {
                        "code" : "iOS6",
                        "role" : ["instructor, coach"]
                    },
                    {
                        "code" : "iOS7",
                        "role" : ["instructor"]
                    }
                ],
            },
        ]
}

@app.route('/api/instructors')
def get_instructors():
    return json.dumps(
        instructors_dump
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
