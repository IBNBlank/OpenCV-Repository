# -*- coding: utf-8 -*-
import cv2
a=cv2.imread("E:\\lesson\\image\\lenacolor.png")
height,width=a.shape[:2]
M=cv2.getRotationMatrix2D((height/2,width/2),45,0.6)
b=cv2.warpAffine(a,M,(height,width))
cv2.imshow("original",a)
cv2.imshow("move",b)
cv2.waitKey()
cv2.destroyAllWindows()
