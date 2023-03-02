import numpy as np
import cv2


cap = cv2.VideoCapture(0)

while(True): 
    ret, frame = cap.read()
    frame = frame[100: int(frame.shape[0]-100), 200: int(frame.shape[1]-200)] 
    cv2.imshow('Video', frame)   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()