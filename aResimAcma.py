import cv2
import numpy as np

img=cv2.imread("630e71c498e600.jpg")
imgGri=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("TOTORO", img)
cv2.imshow("GRI TOTORO", imgGri)

sizeY = img.shape[0]  #genişlik
sizeX = img.shape[1]  #yükseklik
kanal = img.shape[2]  #renkli resimlerde kullanılır

print("yukseklik:", sizeY)
print("genislik:", sizeX)
print("kanal sayisi:", kanal)

cv2.waitKey(0)
cv2.destroyAllWindows()

