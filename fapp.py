from flask import Flask, render_template, url_for, flash, redirect, request
from datetime import datetime
import numpy as np
import os
import urllib.request
from werkzeug.utils import secure_filename
import cv2
from PIL import Image
import face_recognition
import time
from voting import recog

app = Flask(__name__)


app.config['SECRET_KEY'] = 'b007ce7ddab3782a850cbf3ff70187a6'

UPLOAD_FOLDER = 'static/uploads/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])



def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')	
@app.route('/home')
def home():
	return render_template('layout.html')

@app.route('/cam')
def cam():
    rec = recog()
    return redirect(url_for('home'))

if __name__ == "__main__":
	app.run(debug=True)