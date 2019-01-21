# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-01-21 23:01:30
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-01-21 23:17:21

import cv2 as cv

file_path = "..\\example\\image\\lena256.bmp"
image = cv.imread(file_path, cv.IMREAD_UNCHANGED)

### gray to color
# gray to BGR
bgr = cv.cvtColor(image, cv.COLOR_GRAY2BGR)
print(image.shape)
print(bgr.shape)
# split
b, g, r = cv.split(bgr)

### show image
# gray
cv.imshow("gray", image)
# color
cv.imshow("color", bgr)
# single channel
cv.imshow("blue", b)
cv.imshow("green", g)
cv.imshow("red", r)

cv.waitKey(0)
cv.destroyAllWindows()