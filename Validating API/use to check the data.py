
import requests

files = {'files': open('ee.jpg','rb')}
eval = requests.post("http://127.0.0.1:5000/imageload", files = files)
print(eval.text)