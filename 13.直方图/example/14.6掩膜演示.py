# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 17:29:41 2018

@author: 天津拨云咨询服务有限公司  lilizong@gmail.com
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
image=cv2.imread("image\\boat.bmp",0)
mask=np.zeros(image.shape,np.uint8)
mask[200:400,200:400]=255
mi=cv2.bitwise_and(image,mask)
cv2.imshow('original',image)
cv2.imshow('mask',mask)
cv2.imshow('mi',mi)
cv2.waitKey()
cv2.destroyAllWindows()

