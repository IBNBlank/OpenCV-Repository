# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 13:55:27 2018

@author: 天津拨云咨询服务有限公司 lilizong@gmail.com
"""
import cv2
import numpy as np
o = cv2.imread('image\\lena.bmp',cv2.IMREAD_GRAYSCALE)
scharrx = cv2.Sobel(o,cv2.CV_64F,1,0,-1)
scharry = cv2.Sobel(o,cv2.CV_64F,0,1,-1)
scharrx = cv2.convertScaleAbs(scharrx)   # 转回uint8  
scharry = cv2.convertScaleAbs(scharry)  
scharrxy =  cv2.addWeighted(scharrx,0.5,scharry,0.5,0)  
scharrxy11=cv2.Sobel(o,cv2.CV_64F,1,1,-1)
scharrxy11 = cv2.convertScaleAbs(sobelxy11)  
cv2.imshow("original",o)
cv2.imshow("x",scharrx)
cv2.imshow("y",scharry)
cv2.imshow("xy",scharrxy)
cv2.imshow("xy11",scharrxy11)
cv2.waitKey()
cv2.destroyAllWindows()

