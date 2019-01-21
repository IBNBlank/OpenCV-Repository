# -*- coding: utf-8 -*-
"""
Created on Wed May  9 07:47:01 2018

@author: Administrator
"""

import cv2
import numpy as np
a=cv2.imread("image\lenacolor.png",cv2.IMREAD_UNCHANGED)
b=cv2.imread("image\girl.bmp",cv2.IMREAD_UNCHANGED)
face=np.ones((101,101,3))
cv2.imshow("originalA",a)
cv2.imshow("originalB",b)
face=a[220:400,250:350]
b[0:180,0:100]=face
cv2.imshow("result",b)
cv2.waitKey()
cv2.destroyAllWindows()
