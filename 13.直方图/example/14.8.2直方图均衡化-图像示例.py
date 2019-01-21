# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 20:41:08 2018

@author: 天津拨云咨询服务有限公司  lilizong@gmail.com
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
o=cv2.imread("image\\equ.bmp",cv2.IMREAD_GRAYSCALE)
r=cv2.equalizeHist(o)
cv2.imshow("original",o)
cv2.imshow("result",r)
cv2.waitKey()
cv2.destroyAllWindows()
