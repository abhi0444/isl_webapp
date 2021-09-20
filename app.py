from flask import Flask, render_template, request, redirect, url_for, session 
from flask import Flask, render_template
# import tensorflow as tf
# from tensorflow import keras
# import os
# import h5py
# import cv2
# from keras.models import load_model
# from keras.models import Sequential
# from keras.layers import Dense
# from keras.callbacks import ModelCheckpoint
# import numpy
# from keras.models import load_model
# import numpy as np
# from keras.preprocessing import image
 
# import mediapipe as mp
# mp_drawing = mp.solutions.drawing_utils
# mp_holistic = mp.solutions.holistic

import requests
import base64

import os
import json
import cv2
import numpy as np
from werkzeug.utils import secure_filename

UPLOAD_FOLDER='static/uploads/'

app = Flask(__name__) 
app.secret_key = 'hero'
ll = ['A', 'ADD', 'B', 'Bent', 'Between', 'Blind', 'Bottle', 'Brain', 'Bowl', 'C', 'Bud', 'Chest', 'Claw', 'Coolie', 'Cough', 'D', 'Devil', 'Doctor', 'Cow', 'Afraid', 'E', 'East', 'Eight', 'Elbow', 'Evening', 'Eye', 'F', 'Faith', 'Fat', 'Feel', 'Fever', 'Few', 'First', 'Five', 'Food', 'Four', 'G', 'Good', 'Gun', 'Hair', 'Hand', 'Head', 'Hear', 'I', 'Jain', 'K', 'King', 'L', 'Leprosy', 'Love', 'M', 'Me', 'N', 'Nine', 'Nose', 'Nurse', 'O', 'Oath', 'One', 'Open', 'Owl', 'P', 'Police', 'Pray', 'Promise', 'Q', 'R', 'S', 'Seven', 'Shirt', 'Shoulder', 'Sick', 'Six', 'Skin', 'Sleep', 'Soldier', 'Stand', 'Strong', 'Sunday', 'T', 'Telephone', 'Ten', 'Thorn', 'Three', 'Tongue', 'Thumbs_up', 'Trouble', 'Two', 'U', 'V', 'W', 'Word', 'You', 'White', 'X', 'Zero', 'Z', 'Water', 'Wedding', 'West']



@app.route('/')
def login_new():
    return render_template('index.html')

@app.route('/uploader', methods =['GET', 'POST'])
def image_collector():
    if request.method == 'POST':
        file=request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
    
        url = 'http://40.112.61.37:5000/api/'

        img1 = cv2.imread(os.path.join(UPLOAD_FOLDER, filename))
        jpg_img = cv2.imencode('.jpeg', img1)
        my_string = base64.b64encode(jpg_img[1]).decode('utf-8')
       
        # _, im_arr = cv2.imencode('.jpeg', img)  # im_arr: image in Numpy one-dim array format.
        # im = im_arr.tobytes()
        # my_string = base64.b64encode(im)
        
        j_data = json.dumps(my_string)

        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        r = requests.post(url, data=j_data, headers=headers)
        print(r, r.text)
        #host = '0.0.0.0'

    return render_template('index.html',msg=r.text,path = os.path.join(UPLOAD_FOLDER, filename))


if __name__ == '__main__':
       app.run( port = 5000, debug=True)

