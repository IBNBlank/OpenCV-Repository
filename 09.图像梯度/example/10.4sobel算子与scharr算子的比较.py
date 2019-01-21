# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 13:20:34 2018
sobel算子与scharr算子的比较
@author: 天津拨云咨询服务有限公司 lilizong@gmail.com
"""
import cv2
import numpy as np
o = cv2.imread('image\\lena.bmp',cv2.IMREAD_GRAYSCALE)
sobelx = cv2.Sobel(o,cv2.CV_64F,1,0,ksize=3)
sobely = cv2.Sobel(o,cv2.CV_64F,0,1,ksize=3)
sobelx = cv2.convertScaleAbs(sobelx)   # 转回uint8  
sobely = cv2.convertScaleAbs(sobely)  
sobelxy =  cv2.addWeighted(sobelx,0.5,sobely,0.5,0)  

scharrx = cv2.Scharr(o,cv2.CV_64F,1,0)
scharry = cv2.Scharr(o,cv2.CV_64F,0,1)
scharrx = cv2.convertScaleAbs(scharrx)   # 转回uint8  
scharry = cv2.convertScaleAbs(scharry)  
scharrxy =  cv2.addWeighted(scharrx,0.5,scharry,0.5,0) 

cv2.imshow("original",o)
cv2.imshow("sobelxy",sobelxy)
cv2.imshow("scharrxy",scharrxy)
cv2.waitKey()
cv2.destroyAllWindows()