from flask import Flask,request,url_for, render_template, request,send_from_directory,redirect, flash
import os.path
from mongodb import connect_db, db_upload,db_download
from azure_function import azure_upload_file, azure_download_file
from werkzeug.utils import secure_filename
from random import randint



web_site = Flask(__name__)
web_site.secret_key = 'hsjdbf65gfd634dag365aerrt384'
connect_db()
UPLOAD_FOLDER = os.getcwd() + '/buffer/upload_buffer/'
DOWNLOAD_FOLDER = os.getcwd() + '/buffer/download_buffer/'


@web_site.route('/')
def homepage():
	return render_template('homepage.html')


@web_site.route('/upload', methods=['POST','GET'])
def upload_file():
    if(request.method == 'POST'):
        f=request.files['file']
        n = 4
        range_start = 10**(n-1)
        range_end = (10**n)-1
        code = str(randint(range_start, range_end))
        full_name = code + secure_filename(f.filename)
        
        path = UPLOAD_FOLDER + full_name
        f.save(path)
       
        azure_upload_file(full_name,path)#azure
        dic = db_upload(code ,path, full_name)#mongodb
        file_id = str(dic['_id'])
        passkey = str(dic['passkey'])
        message = 'Upload successful\n' + 'file id =' + file_id + '\n passcode = '+ passkey
        flash(message)
    return render_template("upload.html")

@web_site.route('/download', methods=['POST','GET']) 
def download_file():
    if(request.method == 'POST'):
        id = int(request.form['code'])
        passkey = int(request.form['passkey'])
        response = db_download(id,passkey)
        
        if response != None:
            azure_download_file(response["file_name"])
            return send_from_directory(directory=DOWNLOAD_FOLDER, filename=response['file_name'],as_attachment=True)
        else:
            return render_template('download.html')
    return render_template('download.html')

web_site.run(host='0.0.0.0', port=8080, debug=True)