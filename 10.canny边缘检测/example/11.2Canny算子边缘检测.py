# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 14:15:23 2018

sobel算子与scharr算子的比较
@author: 天津拨云咨询服务有限公司 lilizong@gmail.com
"""
import cv2
import numpy as np
o=cv2.imread("image\\lena.bmp",cv2.IMREAD_GRAYSCALE)
r=cv2.Canny(o,100,200)
cv2.imshow("original",o)
cv2.imshow("result",r)
cv2.waitKey()
cv2.destroyAllWindows()
