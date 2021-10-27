#use this if any space is required
# import g/ridfs
import os
import pymongo
import pytz
from datetime import datetime
from random import randint
 


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

def db_upload(code,path,file_name) :
  #https://dev.to/thenishant/store-images-in-mongodb-via-python-2g73
    data_dict = {}
    n = 4
    range_start = 10**(n-1)
    range_end = (10**n)-1
    passkey = randint(range_start, range_end)
    data_dict['_id']= int(code) #generate a fileid
    data_dict['passkey']= passkey
    data_dict['path']= path
    data_dict['file_name'] = file_name
    data_dict['datetime']= caltime()
    db.data_collected.insert_one(data_dict)#user data
    return data_dict


def db_download(file_id,passkey):
    x = db.data_collected.find({"_id":file_id},{'id':1,'passkey':1,'file_name':1})
    for i in x:
        if passkey == i['passkey']:
            print('success')
            return i
        else:
            return None

# connect_db()
# db_upload(1234,1234)
# for x in db.data_collected.find():
#     print(x)

