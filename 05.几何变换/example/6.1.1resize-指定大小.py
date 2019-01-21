# -*- coding: utf-8 -*-
"""
Created on Wed May  9 10:35:04 2018

@author: lilizong@gmail.com
"""
import cv2
a=cv2.imread("image\\lenacolor.png")
b=cv2.resize(a,(200,100))
#注意：第2个参数控制的是“列长度、行长度”，注意顺序。
cv2.imshow("original",a)
cv2.imshow("resize",b)
cv2.waitKey()
cv2.destroyAllWindows()
