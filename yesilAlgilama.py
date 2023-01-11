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
  
    contours, hierarchy = cv2.findContours(greenMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  
    if len(contours)  != 0:
        for contour in contours:
            if cv2.contourArea(contour) > 500:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 0, 255), 3)
  
    cv2.imshow("WEBCAM", frame)
    #cv2.imshow("GREEN MASK", greenMask)
    cv2.imshow("GREEN", green)
    
    if cv2.waitKey(1) & 0xFF == ord("b"):
        break
    
cap.release()
cv2.destroyAllWindows()    
    