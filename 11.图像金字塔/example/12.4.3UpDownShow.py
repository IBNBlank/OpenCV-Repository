# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 09:12:13 2018
比较向上取样后再次向下取样后的结果
@author: 天津拨云咨询服务有限公司  lilizong@gmail.com
"""
import cv2
o=cv2.imread("image\\girl.bmp")
r=cv2.pyrUp(o)
r2=cv2.pyrDown(r)
diff=r2-o
cv2.imshow("difference",diff)
cv2.waitKey()
cv2.destroyAllWindows()