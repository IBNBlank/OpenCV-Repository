# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-01-20 23:17:47
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-01-20 23:22:30

import cv2 as cv

gray_path = "..\\example\\image\\lena256.bmp"
gray = cv.imread(gray_path, cv.IMREAD_UNCHANGED)

color_path = "..\\example\\image\\lenacolor.png"
color = cv.imread(color_path, cv.IMREAD_UNCHANGED)

### shape
print(gray.shape)
print(color.shape)

### size
print(gray.size)
print(color.size)

### dtype
print(gray.dtype)
print(color.dtype)