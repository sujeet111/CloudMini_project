from flask import Flask,request,url_for, render_template, request, send_file
from flask_pymongo import PyMongo
from mongodb import connect_db, db_upload,db_download

web_site = Flask(__name__)
connect_db()
# mongo=PyMongo(web_site)


@web_site.route('/')
#nothing required here ig
def index():
	return render_template('index.html')




@web_site.route('/upload', methods=['POST'])
								# https://www.javatpoint.com/flask-file-uploading
								# https://www.youtube.com/watch?v=DsgAuceHha4&ab_channel=PrettyPrinted
def upload_file():
  passkey= ''
  file_contents= ''		#file loc
  email= ''						#user email
  to_email= ''
  # if 'email' in request.file:
	# 		email=request.file['email']
	# 		mongo.save_file(email.fileanme, email)

	# if 'to_email' in request.file:
	# 		to_email=request.file['to_email']
	# 		mongo.save_file(to_email.fileanme, to_email)

	# if 'passkey' in request.file:
	# 		passkey=request.file['passkey']
	# 		mongo.save_file(passkey.fileanme, passkey)
  										#code for file upload
  # file_id = db_upload(passkey, file_contents, email, to_email)	#returns generated file_id 
	# return render_template('upload.html', file_id= file_id)
  pass




@web_site.route('/download') 
# https://roytuts.com/how-to-download-file-using-python-flask/
# https://www.youtube.com/watch?v=DsgAuceHha4&ab_channel=PrettyPrinted
#code for file download(ask for file id)
#pass file_id to next function
def download_file():
  return render_template('download.html')


@web_site.route('/download/<file_id>') 
#automatically start download and show send back to index with meta data
#if image, the page should display the image along with some details;
def retrivefile(file_id):
  x = db_download(file_id)
  user_passwd = ''
  # if x.passkey == user_passwd:
  #   pass

  # # return



web_site.run(host='0.0.0.0', port=8080)