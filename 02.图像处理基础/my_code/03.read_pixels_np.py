# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-01-20 20:02:51
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-01-20 23:04:25

import cv2 as cv
import numpy as np

gray_path = "..\\example\\image\\lena256.bmp"
gray = cv.imread(gray_path, cv.IMREAD_UNCHANGED)

color_path = "..\\example\\image\\lenacolor.png"
color = cv.imread(color_path, cv.IMREAD_UNCHANGED)

### gray image
gray_pixel = gray.item(100, 100)
print(gray_pixel)

### color image
# blue
blue_pixel = color.item(100, 100, 0)
print(blue_pixel)
# green
green_pixel = color.item(100, 100, 1)
print(green_pixel)
# red
red_pixel = color.item(100, 100, 2)
print(red_pixel)