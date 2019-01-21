# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 09:12:13 2018

@author: 天津拨云咨询服务有限公司  lilizong@gmail.com
"""
import cv2
o=cv2.imread("image\\girl.bmp")
up=cv2.pyrUp(o)
down=cv2.pyrDown(up)
cv2.imshow("original",o)
cv2.imshow("up",up)
cv2.imshow("down",down)
cv2.waitKey()
cv2.destroyAllWindows()