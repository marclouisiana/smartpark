import numpy as np
import cv2

rect = (0,0,0,0)
startPoint = False
endPoint = False
f = open('map.txt', 'w')

def on_mouse(event,x,y,flags,params):

    global rect,startPoint,endPoint

    # get mouse click
    if event == cv2.EVENT_LBUTTONDOWN:

        if startPoint == True and endPoint == True:
            startPoint = False
            endPoint = False
            rect = (0, 0, 0, 0)

        if startPoint == False:
            rect = (x, y, 0, 0)
            startPoint = True
        elif endPoint == False:
            rect = (rect[0], rect[1], x, y)
            endPoint = True

cap = cv2.VideoCapture(1)
cap.set(3,1920)
cap.set(4,1080)

waitTime = 50

#Reading the first frame
(grabbed, frame) = cap.read()

while(cap.isOpened()):

    (grabbed, frame) = cap.read()

    cv2.namedWindow('frame')
    cv2.moveWindow('frame',0,0)
    cv2.setMouseCallback('frame', on_mouse)

    #drawing rectangle
    if startPoint == True and endPoint == True:
        cv2.rectangle(frame, (rect[0], rect[1]), (rect[2], rect[3]), (255, 0, 255), 2)
        f.write(str(rect[0]) + ' ' + str(rect[1]) + ' ' + str(rect[2]) + ' ' + str(rect[3]) + " ")
        startPoint = False
        endPoint = False

    cv2.imshow('frame',frame)

    key = cv2.waitKey(waitTime)

    if key == 27:
        break

f.close()
cap.release()
cv2.destroyAllWindows()
