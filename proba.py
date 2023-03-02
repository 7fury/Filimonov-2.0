import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
cap = cv.VideoCapture(0)
img1 = cv.imread('/home/it-14/Рабочий стол/Filimonov 2.0/pudge.jpg',cv.IMREAD_GRAYSCALE)  
sift = cv.SIFT_create()
bf = cv.BFMatcher()
kp1, des1 = orb.detectAndCompute(img1,None)
while(True): 
    ret , frame = cap.read()
    kp2, des2 = orb.detectAndCompute(img2,None)
    matches = bf.match(des1,des2)
    img2 = cap.read()
    cv.imshow('Video', frame)   
    good = []
    for m,n in matches:
        if m.distance < 0.75*n.distance:
            good.append([m])
# cv.drawMatchesKnn expects list of lists as matches.
    img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    cv.imshow('aa', cv.resize(img3, (1000,650)))
    if cv.waitKey(1) & 0xFF == ord('q'):
        break