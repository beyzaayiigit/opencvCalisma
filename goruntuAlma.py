import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while 1:
    ret, frame = cap.read()
    
    frame = cv2.flip(frame, 1)
    cv2.imshow("WEBCAM", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("b"):
        break
    
cap.release()
cv2.destroyAllWindows()    
    