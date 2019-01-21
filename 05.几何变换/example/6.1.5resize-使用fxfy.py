# -*- coding: utf-8 -*-
"""
Created on Wed May  9 10:35:04 2018

@author: lilizong@gmail.com
"""
import cv2
import numpy as np
a=cv2.imread("image\\lenacolor.png")
b=cv2.resize(a,None,fx=1.2,fy=0.5)
cv2.imshow("original",a)
cv2.imshow("resize",b)
cv2.waitKey()
cv2.destroyAllWindows()
