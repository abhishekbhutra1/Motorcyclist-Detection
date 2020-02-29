# Python code for Background subtraction using OpenCV
import numpy as np
import cv2

cap = cv2.VideoCapture("T2.mp4")
fgbg = cv2.createBackgroundSubtractorMOG2()

while (1):
    ret, frame = cap.read()
    frame1 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    filter = cv2.GaussianBlur(frame1,(5,5),100)
    fgmask = fgbg.apply(filter)
    contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for c in contours:
        area = cv2.contourArea(c)
        if (area > 1000):
            x,y,w,h = cv2.boundingRect(c)
            #detecting bike without helmet........
            #if bike without helmet then ..
            img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('image', img)
    cv2.imshow('frame', frame1)
    cv2.imshow('fgmask', fgmask)
    k = cv2.waitKey(50)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
