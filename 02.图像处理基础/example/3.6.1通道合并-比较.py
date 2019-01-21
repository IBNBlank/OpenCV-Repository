# -*- coding: utf-8 -*-
"""
Created on Wed May  9 10:33:16 2018

@author: lilizong@gmail.com
"""

import cv2
import numpy as np
a=cv2.imread("image\lenacolor.png")
b,g,r=cv2.split(a)
bgr=cv2.merge([b,g,r])
rgb=cv2.merge([r,g,b])
cv2.imshow("bgr",bgr)
cv2.imshow("rgb",rgb)
cv2.waitKey()
cv2.destroyAllWindows()
