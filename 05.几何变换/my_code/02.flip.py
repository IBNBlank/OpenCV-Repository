# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-04-25 14:10:38
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-04-26 00:34:39

import cv2 as cv

file_path = "..\\example\\image\\lenacolor.png"
image = cv.imread(file_path, cv.IMREAD_UNCHANGED)

### flip
# X axis
img_x = cv.flip(image, 0)
# Y axis
img_y = cv.flip(image, 1)
# XY
img_xy = cv.flip(image, -1)

### show image
# origin
cv.imshow("origin", image)
# X axis
cv.imshow("X", img_x)
# Y axis
cv.imshow("Y", img_y)
# XY
cv.imshow("XY", img_xy)

cv.waitKey(0)
cv.destroyAllWindows()