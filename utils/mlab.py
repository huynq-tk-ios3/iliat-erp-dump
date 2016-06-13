import mongoengine

host = "ds019053.mlab.com"
port = 19053
db_name = "erp-dump"
user_name = "admin"
password = "admin"

uri = "mongodb://admin:admin@ds019053.mlab.com:19053/erp-dump"
db = None

def connect():
    db = mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def disconnect():
    if db != None:
        db.close()
