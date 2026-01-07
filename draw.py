import cv2 as cv
import numpy as np

blank = np.zeros((500,500, 3), dtype='uint8')
# uint8 is data type of an image
cv.imshow('Blank', blank)

# 1. Paint image a certain colour
blank[200:300, 300:400] = 0, 0, 255
cv.imshow('Green', blank)

# 2. Draw a rectangle

cv.waitKey(0)