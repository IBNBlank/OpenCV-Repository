# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 11:30:20 2018

@author: 天津拨云咨询服务有限公司 lilizong@gmail.com
"""
import cv2
import numpy as np
o=cv2.imread("image\\man.bmp")
r1=cv2.pyrDown(o)
r2=cv2.pyrDown(r1)
r3=cv2.pyrDown(r2)
cv2.imshow("original",o)
cv2.imshow("PyrDown1",r1)
cv2.imshow("PyrDown2",r2)
cv2.imshow("PyrDown3",r3)
cv2.waitKey()
cv2.destroyAllWindows()
