# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 11:45:06 2018

@author: Administrator
"""
import cv2
import numpy as np
o = cv2.imread('image\\contours.bmp')  
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
image, contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  
co=o.copy()
r=cv2.drawContours(co,contours,2,(0,0,255),6)  
cv2.imshow("original",o)
cv2.imshow("contours",r)
cv2.waitKey()
cv2.destroyAllWindows()

