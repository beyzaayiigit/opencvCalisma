import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    
    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lowerGreen = np.array([45, 100, 50])
    upperGreen = np.array([75, 255, 255])
    
    greenMask = cv2.inRange(hsvFrame, lowerGreen, upperGreen) 
    green = cv2.bitwise_and(frame, frame, mask = greenMask)   
  
    cv2.imshow("WEBCAM", frame)
    #cv2.imshow("GREEN MASK", greenMask)
    cv2.imshow("GREEN", green)
    
    if cv2.waitKey(1) & 0xFF == ord("b"):
        break
    
cap.release()
cv2.destroyAllWindows()    
    