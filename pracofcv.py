import  numpy as np
import cv2

img = cv2.imread('test14.jpg',0)
cv2.imshow('floppy',img)
k = cv2.waitKey(0)
if(k==27):
  cv2.destroyWindow()
elif(k== ord('s')):
    cv2.imwrite('iggygyray.png',img)
    cv2.destroyWindow('floppy')