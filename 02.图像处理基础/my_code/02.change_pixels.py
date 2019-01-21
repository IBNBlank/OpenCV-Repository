# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-01-20 19:32:33
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-01-20 19:55:27

import cv2 as cv

gray_path = "..\\example\\image\\lena256.bmp"
gray = cv.imread(gray_path, cv.IMREAD_UNCHANGED)

color_path = "..\\example\\image\\lenacolor.png"
color = cv.imread(color_path, cv.IMREAD_UNCHANGED)

### gray image
print(gray[100, 100])
gray[100, 100] = 255
print(gray[100, 100])

### color image
# blue
print(color[100, 100, 0])
color[100, 100, 0] = 255
print(color[100, 100, 0])
# green
print(color[100, 100, 1])
color[100, 100, 1] = 255
print(color[100, 100, 1])
# red
print(color[100, 100, 2])
color[100, 100, 2] = 255
print(color[100, 100, 2])
# all
print(color[100, 100])
color[100, 100] = [0, 0, 0]
print(color[100, 100])
# block
color[100:150, 100:150] = [255, 255, 255]
cv.imshow("result", color)
cv.waitKey(0)
cv.destroyAllWindows()