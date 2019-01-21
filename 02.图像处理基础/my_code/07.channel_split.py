# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-01-20 23:48:21
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-01-21 00:31:10

import cv2 as cv
import numpy as np

file_path = "..\\example\\image\\lenacolor.png"
image = cv.imread(file_path, cv.IMREAD_UNCHANGED)

### split
# split all channels
# blue, green, red = cv.split(image)
# split each channel
blue = cv.split(image)[0]
green = cv.split(image)[1]
red = cv.split(image)[2]
# show
cv.imshow("blue", blue)
cv.imshow("green", green)
cv.imshow("red", red)

cv.waitKey(0)
cv.destroyAllWindows()