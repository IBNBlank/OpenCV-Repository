# -*- coding: utf-8 -*-
"""
Created on Mon Jul  10 10:26:57 2018

@author:  天津拨云咨询服务有限公司  lilizong@gmail.com
"""

import cv2
import matplotlib.pyplot as plt
img = cv2.imread('image\\boat.bmp',cv2.IMREAD_GRAYSCALE)
equ = cv2.equalizeHist(img)
plt.subplot(221)
plt.imshow(img,cmap=plt.cm.gray),plt.axis('off')
plt.subplot(222)
plt.imshow(equ,cmap=plt.cm.gray),plt.axis('off')
plt.subplot(223)
plt.hist(img.ravel(),256)
plt.subplot(224)
plt.hist(equ.ravel(),256)