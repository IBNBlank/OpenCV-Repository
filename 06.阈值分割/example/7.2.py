# -*- coding: utf-8 -*-
"""
Created on Sun May 13 10:57:39 2018

@author: Administrator
"""
import cv2
a=cv2.imread("image\\lena512.bmp",cv2.IMREAD_UNCHANGED)
#注意原始图像的类型，必须是8位单通道图像,彩色图像无意义
r,b=cv2.threshold(a,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow("a",a)
cv2.imshow("b",b)
print(r)
cv2.waitKey()
cv2.destroyAllWindows()

