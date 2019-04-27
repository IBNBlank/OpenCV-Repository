# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-04-28 00:51:34
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-04-28 01:22:57

import cv2 as cv
import numpy as np

file_path = "..\\example\\image\\contours.bmp"
image = cv.imread(file_path, cv.IMREAD_UNCHANGED)

### contours
# find
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
contours, hierarchy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# draw
img_fin = image.copy()
img_fin = cv.drawContours(img_fin, contours, -1, (0,0,255), 6)

### show image
# origin
cv.imshow("origin", image)
# contours
cv.imshow("countours", img_fin)

cv.waitKey(0)
cv.destroyAllWindows()