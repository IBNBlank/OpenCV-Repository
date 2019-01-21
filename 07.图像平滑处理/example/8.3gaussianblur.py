# -*- coding: utf-8 -*-
"""
Created on Sun May 13 18:10:47 2018

@author: lilizong@gmail.com
"""

import cv2
o=cv2.imread("image\\lenaNoise.png")
r=cv2.GaussianBlur(o,(3,3),0)
cv2.imshow("original",o)
cv2.imshow("result",r)
cv2.waitKey()
cv2.destroyAllWindows()