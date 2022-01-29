from flask import Flask, Response, request, jsonify, redirect, url_for 
import cv2
import numpy as np
import keras
import os


def character_recog(image_path):
  img_arr=[]
  gray = cv2.imread(image_path, cv2.COLOR_BGR2GRAY)
  reteval, img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
  img = cv2.resize(img, (32,32), interpolation=cv2.INTER_AREA)
  img = np.reshape(np.array(img), (32,32,1))
  img_arr.append(img)
  img_arr = np.array(img_arr)
  model = keras.models.load_model("lenetmodel")
  result = model.predict(img_arr)
  return int(np.argmax(result[0]))

app = Flask(__name__)

@app.route('/imageload', methods = ['POST'])
def loadImage():
  if request.method == 'POST':
    temp_file = request.files['files']
    temp_file.save(temp_file.filename)
    result =character_recog(temp_file.filename)
    os.remove(temp_file.filename)
    return jsonify({'result': result})

if __name__ == "__main__":
  app.run() 