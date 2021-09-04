#use this if any space is required
# import g/ridfs
import os
import pymongo
import pytz
from datetime import datetime


def caltime():
  IST = pytz.timezone('Asia/Kolkata')
  datetime_ist = datetime.now(IST)
  return str(datetime_ist)

#mongodb code (Do not touch)
def connect_db():
  print('*'*1,"Setting up Mongo Client",'*'*1)
  dbpassword = os.environ['dbpassword']
  print('*'*2,'Connecting to database','*'*2)
  client = pymongo.MongoClient("mongodb+srv://sujeet:"+ dbpassword +"@cluster0.42z3v.mongodb.net/user_data_db?retryWrites=true&w=majority")
  global db
  db = client.user_data_db
  print('*'*3,'connected to Mongodb database:',db.name,'*'*3)

def db_upload(passkey, file_loc = '', email = '', to_email = '') :
  #https://dev.to/thenishant/store-images-in-mongodb-via-python-2g73
  data_dict = {}
  data_dict['file_id']= '' #generate a fileid
  data_dict['passkey']= passkey
  data_dict['file_contents']= ''
  data_dict['email']= email
  data_dict['to_email']= to_email
  data_dict['datetime']= caltime()
  db.data_collected.insert_one(data_dict)#user data

  # fs = gridfs.GridFS(db)
  # with open(file_loc, 'rb') as f:
  #   contents = f.read()
  # fs.put(contents,file_id= file_id)
  # return data_dict('file_id')


def db_download(file_id):
  x = db.data_collected.find({"file_id":file_id})
  # x.file_id
  # x.file
  return x

# connect_db()
# db_upload(1234,1234)
# for x in db.data_collected.find():
#     print(x)

