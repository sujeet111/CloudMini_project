#use this if any space is required
import gridfs
import os
import pymongo
from datetime import datetime


#mongodb code (Do not touch)
def connect_db():
  print('*'*1,"Setting up Mongo Client",'*'*1)
  dbpassword = os.environ['dbpassword']
  print('*'*2,'Connecting to database','*'*2)
  client = pymongo.MongoClient("mongodb+srv://sujeet:"+ dbpassword +"@cluster0.42z3v.mongodb.net/user_data_db?retryWrites=true&w=majority")
  global db
  db = client.data_collected
  print('*'*3,'connected to Mongodb database: ',db.name,'*'*3)

def db_upload(passkey='', file_contents = '', email = '', to_email = ''):
  data_dict = {}
  data_dict['file_id']= '' #generate a fileid
  data_dict['passkey']= passkey
  data_dict['file_contents']= file_contents
  data_dict['email']= email
  data_dict['to_email']= to_email
  data_dict['datetime']= str(datetime)
  print(db.name)
  s=db.data_collected.insert_one(data_dict)
  print(s)
  # return data_dict('file_id')

connect_db()
db_upload()
for x in db.data_collected.find():
    print(x)