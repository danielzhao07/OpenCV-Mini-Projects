import cv2 as cv

# img = cv.imread('Resources/Photos/cat_large.jpg') # read image

# cv.imshow('Cat', img) # diplay image

# cv.waitKey(0) # wait for key to be pressed

# Reading videos

capture = cv.VideoCapture('Resources/Videos/dog.mp4') # int 0 for webcam, 1 first camera, 2 second camera, etc

while True:
    isTrue, frame = capture.read() # returns frame, and bol whether video was read
    cv.imshow('Video', frame) # show video and pass in frame

    if cv.waitKey(20) & 0xFF==ord('d'): # break out of video | if letter d is pressed, end the video
        break

capture.release() # release capture poijnter

cv.destroyAllWindows() # destroy all windows
