# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 13:55:27 2018

@author: 天津拨云咨询服务有限公司 lilizong@gmail.com
"""
import cv2
import numpy as np
o = cv2.imread('image\\lena.bmp',cv2.IMREAD_GRAYSCALE)
laplacian = cv2.Laplacian(o,cv2.CV_64F)
laplacian = cv2.convertScaleAbs(laplacian)   # 转回uint8 
cv2.imshow("original",o)
cv2.imshow("laplacian",laplacian)
cv2.waitKey()
cv2.destroyAllWindows()

