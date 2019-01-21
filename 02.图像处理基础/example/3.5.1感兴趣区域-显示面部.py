# -*- coding: utf-8 -*-
"""
Created on Wed May  9 07:47:01 2018

@author: Administrator
"""

import cv2
import numpy as np
a=cv2.imread("image\lenacolor.png",cv2.IMREAD_UNCHANGED)
face=np.ones((101,101,3))
cv2.imshow("original",a)
face=a[220:400,250:350]
cv2.imshow("face",face)
cv2.waitKey()
cv2.destroyAllWindows()
