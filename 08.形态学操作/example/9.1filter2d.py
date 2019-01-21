# -*- coding: utf-8 -*-
"""
Created on Sun May 13 13:40:26 2018

@author: Administrator
"""
import cv2
import numpy as np
o=cv2.imread("image\lenacolor.png")
f=np.array([[0,1,0],[1,-4,1],[0,1,0]])  
r=cv2.filter2D(o,-1,f)
cv2.imshow("original",o)
cv2.imshow("result",r)
cv2.waitKey()
cv2.destroyAllWindows()
