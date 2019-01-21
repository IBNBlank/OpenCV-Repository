# -*- coding: utf-8 -*-
"""
Created on Mon May  7 18:18:51 2018

@author: lilizong@gmail.com
"""
import cv2
a=cv2.imread("image\lena256.bmp",cv2.IMREAD_UNCHANGED)
b=cv2.imread("image\lenacolor.png",cv2.IMREAD_UNCHANGED)
print(a.shape)
print(b.shape)
print(a.size)
print(b.size)
print(a.dtype)
print(b.dtype)

