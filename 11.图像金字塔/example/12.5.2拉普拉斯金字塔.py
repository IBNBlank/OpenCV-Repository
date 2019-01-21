# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 09:12:13 2018
比较向上取样后再次向下取样后的结果
@author: 天津拨云咨询服务有限公司  lilizong@gmail.com
"""
import cv2
o=cv2.imread("image\\lena.bmp")
od=cv2.pyrDown(o)
odu=cv2.pyrUp(od)
lapPyr=o-odu
o1=od
o1d=cv2.pyrDown(o1)
o1du=cv2.pyrUp(o1d)
lapPyr1=o1-o1du
cv2.imshow("lapPyr",lapPyr)
cv2.imshow("lapPry1",lapPyr1)
cv2.waitKey()
cv2.destroyAllWindows()
