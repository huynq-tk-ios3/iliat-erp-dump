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
def hello_world():
    return "Iliat GMATers, don't panic!"
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

@app.route('/api/instructor?code=<instructor_code>')
def get_instructor(instructor_code):
    ret_list = []
    for instructor in instructors_dump["items"]:
        if instructor["code"] == instructor_code:
            ret_list.append(instructor)
    return json.dumps(
        ret_list
    )
# @app.route('/api/intructors')
# def get_instructors():
#     return json.dumps(
#     {
#         "items": [
#             {
#                 "name" : "Nguyễn Sơn Vũ",
#                 "team" : "iOS",
#                 "classes" : [
#                     {
#                         "code" : "iOS5",
#                         "role" : ["coach", "instructor"]
#                     },
#                     {
#                         "code" : "iOS6",
#                         "role" : ["instructor"]
#                     }
#                 ],
#                 "code" : "002004",
#                 "image" : [
#                     "small": "http://imgur.com/E3zFiyK",
#                     "large": "http://imgur.com/a/GyUUC"
#                 ]
#             }
#         ]
#     })

@app.route('/api/test-deploy')
def test_deploy():
    return "deploy 0.0.1"

@app.route('/api/question_type')
def get_gmat_question_type():
    return json.dumps({"type":
                           [
                               {"code" : "SC",
                                "detail":"Sentence Correction",
                                "sub_types": [
                                    {"code": "MISC",
                                     "detail": "Miscellaneous"}
                                ]},
                               {"code" : "CR",
                                 "detail":"Critical Reasoning",
                                "sub_types": [
                                    {"code": "MBT",
                                     "detail": "Must be true"},
                                    {"code": "W",
                                     "detail": "Weaken"},
                                    {"code": "S",
                                     "detail": "Strengthen"},
                                    {"code": "E",
                                     "detail": "Evaluate"},
                                    {"code": "A",
                                     "detail": "Assumption"},
                                    {"code": "RTP",
                                     "detail": "Resolve the paradox"},
                                    {"code": "BF",
                                     "detail": "Bold face"},
                                    {"code": "MISC",
                                     "detail": "Miscellaneous"}
                                ]
                                },
                               {"code" : "RC",
                                "detail":"Reading Comprehension",
                                "sub_types": [
                                    {"code": "MI",
                                     "detail": "Main Idea"},
                                    {"code": "D",
                                     "detail": "Detail"},
                                    {"code": "INF",
                                     "detail": "Inference"},
                                    {"code": "OOC",
                                     "detail": "Out of context"},
                                    {"code": "LS",
                                     "detail": "Logical structure"},
                                    {"code": "AT",
                                     "detail": "Author's tone"},
                                    {"code": "MISC",
                                     "detail": "Miscellaneous"}
                                ]},
                               {"code" : "Q",
                                "detail":"Quantitative",
                                "sub_types": [
                                    {"code": "ARTH",
                                     "detail": "Arithmetic"},
                                    {"code": "ALG",
                                     "detail": "Algebra"},
                                    {"code": "GEO",
                                     "detail": "Geometry"},
                                    {"code": "WP",
                                     "detail": "World Problems"},
                                    {"code": "MISC",
                                     "detail": "Miscellaneous"}
                                ]}
                           ]});

@app.route('/api/question', methods=['POST'])
def get_question():
    list_id_question = request.form.getlist('question_id')
    questions_reponse = []
    questions = Question.objects
    for id in list_id_question:
        question = questions.get(id=ObjectId(id))
        questions_reponse.append(question)
    question_collection = QuestionCollection(questions = questions_reponse)
    return remove_dollar_sign(str(question_collection.to_json()))


@app.route('/api/question_collection')
@app.route('/api/questions')
def get_gmat_question_collection():
    questions = Question.objects
    question_collection = QuestionCollection(questions=questions)
    return remove_dollar_sign(str(question_collection.to_json()))

@app.route('/api/techkids/login')
def get_login_techkids():
    username = request.args.get('username')
    password = request.args.get('password')
    for user in User.objects(user_name=username):
        if (user.password == password):
            return json.dumps({"login_status": 1, "login_message": "Login Success", "link":"http://iliat.org/download.txt"})
    return json.dumps({"login_status": 0, "login_message": "Login Failed"})


@app.route('/api/question_pack_collection')
@app.route('/api/question_packs')
def get_gmat_question_pack_collection():
    question_packs = QuestionPack.objects
    question_pack_collection = QuestionPackCollection(question_packs = question_packs)
    return remove_dollar_sign(str(question_pack_collection.to_json()))

@app.route('/api/version')
def get_gmat_version():
    version = Version.objects[0]
    return remove_dollar_sign(str(version.to_json()))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9696)
