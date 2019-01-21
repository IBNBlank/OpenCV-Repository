# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 17:03:50 2018
@author: 天津拨云咨询服务有限公司  lilizong@gmail.com
"""
import cv2
import matplotlib.pyplot as plt
o=cv2.imread("image\\boat.jpg")
cv2.imshow("original",o)
plt.hist(o.ravel(),256)
cv2.waitKey()
cv2.destroyAllWindows()