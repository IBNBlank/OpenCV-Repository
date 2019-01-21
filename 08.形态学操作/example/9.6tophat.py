# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 09:17:53 2018

@author: 天津拨云咨询服务有限公司 lilizong@gmail.com
"""
import cv2
import numpy as np
o=cv2.imread("image\\tophat.bmp",cv2.IMREAD_UNCHANGED)
k=np.ones((5,5),np.uint8)
r=cv2.morphologyEx(o,cv2.MORPH_TOPHAT,k)
cv2.imshow("original",o)
cv2.imshow("result",r)
cv2.waitKey()
cv2.destroyAllWindows()
