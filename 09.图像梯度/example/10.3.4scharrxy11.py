# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 13:55:27 2018

@author: 天津拨云咨询服务有限公司 lilizong@gmail.com
"""
import cv2
import numpy as np
o = cv2.imread('image\\scharr.bmp',cv2.IMREAD_GRAYSCALE)
scharrxy11=cv2.Scharr(o,cv2.CV_64F,1,1)
cv2.imshow("original",o)
cv2.imshow("xy11",scharrxy11)
cv2.waitKey()
cv2.destroyAllWindows()


#此时会报错：
# error: (-215) dx >= 0 && dy >= 0 && dx+dy == 1
# in function cv::getScharrKernels
