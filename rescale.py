import cv2 as cv

img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('Cat', img)

# resize frame to particular scale value/dimension
def rescaleFrame(frame, scale = 0.75):
    # images, videos and live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale) # convert float to int
    
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)

def changeRes(width,height):
    # only works with live video
    capture.set(3, width) # 3 is width
    capture.set(4, height) # 4 is height

# Reading videos
capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read() # returns frame, and bol whether video was read
    
    frame_resized = rescaleFrame(frame, scale = 0.2) # pass frame to resize function
    
    cv.imshow('Video', frame) # show video and pass in frame
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'): # break out of video | if letter d is pressed, end the video
        break

capture.release() 

cv.destroyAllWindows() 