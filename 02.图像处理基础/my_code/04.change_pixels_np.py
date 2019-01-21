# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-01-20 20:03:12
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-01-20 23:15:15

import cv2 as cv
import numpy as np

gray_path = "..\\example\\image\\lena256.bmp"
gray = cv.imread(gray_path, cv.IMREAD_UNCHANGED)

color_path = "..\\example\\image\\lenacolor.png"
color = cv.imread(color_path, cv.IMREAD_UNCHANGED)

### gray image
print(gray.item(100, 100))
gray.itemset((100, 100), 255)
print(gray.item(100, 100))

### color image
# blue
print(color.item(100, 100, 0))
color.itemset((100, 100, 0), 255)
print(color.item(100, 100, 0))
# green
print(color.item(100, 100, 1))
color.itemset((100, 100, 1), 255)
print(color.item(100, 100, 1))
# red
print(color.item(100, 100, 2))
color.itemset((100, 100, 2), 255)
print(color.item(100, 100, 2))