from flask import Flask, render_template, request, send_file
from mongodb import connect_db, db_upload,db

web_site = Flask(__name__)
connect_db()
@web_site.route('/')
#nothing required here ig
def index():
	return render_template('index.html')


@web_site.route('/upload') #https://www.javatpoint.com/flask-file-uploading
def upload_file():#code for file upload
  return render_template('upload.html')


@web_site.route('/download') 
#https://roytuts.com/how-to-download-file-using-python-flask/
#code for file download(ask for file id)
#pass file_id to next function
def download_file():
  return render_template('download.html')


@web_site.route('/download/<file_id>') 
#automatically start download and show send back to index with meta data
#if image, the page should display the image along with some details;
def retrivefile(file_id):
  file_loc = "" #will get from db
  return send_file(file_loc, as_attachment=True)




web_site.run(host='0.0.0.0', port=8080)