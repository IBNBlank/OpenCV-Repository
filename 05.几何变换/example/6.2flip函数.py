# -*- coding: utf-8 -*-
import cv2
a=cv2.imread("E:\\lesson\\image\\lenacolor.png")
b=cv2.flip(a,-1)
cv2.imshow("original",a)
cv2.imshow("flip",b)
cv2.waitKey()
cv2.destroyAllWindows()
