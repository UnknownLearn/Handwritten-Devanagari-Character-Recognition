import os
import cv2
import numpy as np

images = "images/"

for image in os.listdir(images):
    path = images+ str(image)
    print(path)
    img = cv2.imread(images+ str(image))
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    img = cv2.filter2D(img, -1, kernel)
    img = img[10:80,10:80]
    img = cv2.resize(img, (32,32), interpolation=cv2.INTER_AREA)
    cv2.imwrite(path,img)