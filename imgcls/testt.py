import os,cv2
import sys
oriimg = cv2.imread("car.png",0)
img = cv2.resize(oriimg,(360,480))
cv2.imwrite("resizeimg.png",newimg)
