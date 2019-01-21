# -*- coding: utf-8 -*-
"""
Created on Mon May 14 11:18:05 2018

@author: 天津拨云咨询服务有限公司   lilizong@gmail.com
"""
import cv2
o=cv2.imread("image\\lenaNoise.png")
r=cv2.medianBlur(o,3)
cv2.imshow("original",o)
cv2.imshow("result",r)
cv2.waitKey()
cv2.destroyAllWindows()

