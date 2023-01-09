import cv2
import numpy as np

img=cv2.imread("630e71c498e60.jpg")
imgGri=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("totoro", img)
cv2.imshow("gri totoro", imgGri)

size_y = img.shape[0]  #genişlik
size_x = img.shape[1]  #yükseklik
kanal = img.shape[2]  #renkli resimlerde kullanılır

print("yükseklik:", size_y)
print("genişlik:", size_x)
print("kanal sayısı:", kanal)

cv2.waitKey(0)
cv2.destroyAllWindows()

