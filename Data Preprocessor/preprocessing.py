import os
import cv2

images = "collected data/"

for image in os.listdir(images):
    path = images+ str(image)
    print(path)
    img = cv2.imread(images+ str(image))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    reteval, img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    img = cv2.resize(img, (32,32), interpolation=cv2.INTER_AREA)
    cv2.imwrite(path,img)