# -*- coding: utf-8 -*-
"""
Created on Wed May  9 10:35:04 2018

@author: lilizong@gmail.com
"""
import cv2
a=cv2.imread("image\\lena256.bmp",cv2.IMREAD_UNCHANGED)
b=cv2.cvtColor(a,cv2.COLOR_GRAY2BGR)
print(a.shape)
print(b.shape)