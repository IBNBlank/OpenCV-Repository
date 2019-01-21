# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 17:03:50 2018
@author: lilizong@gmail.com
"""
import cv2
import numpy as np
img=cv2.imread("image\\boat.jpg")
hist = cv2.calcHist([img],[0],None,[256],[0,255])
print(type(hist))
print(hist.size)
print(hist.shape)
print(hist)
