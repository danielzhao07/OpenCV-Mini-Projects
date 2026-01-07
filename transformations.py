import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')

cv.imshow('Boston', img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0]) # 1 - width, 0 - height
    return cv.warpAffine(img, transMat, dimensions)

# -x -> Left -y -> Up

translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

cv.waitKey(0)