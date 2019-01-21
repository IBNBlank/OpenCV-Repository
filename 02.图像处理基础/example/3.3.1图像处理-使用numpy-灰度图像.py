# -*- coding: utf-8 -*-
"""
Created on Mon May  7 11:11:49 2018

@author: lilizong@gmail.com
"""
import cv2
import numpy as np
i=cv2.imread("image\lena256.bmp",cv2.IMREAD_UNCHANGED)

print(i.item(100,100))
i.itemset((100,100),255)
print(i.item(100,100))