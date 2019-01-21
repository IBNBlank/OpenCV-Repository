# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-01-21 23:00:06
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-01-21 23:05:31

import cv2 as cv

file_path = "..\\example\\image\\lenacolor.png"
image = cv.imread(file_path, cv.IMREAD_UNCHANGED)

### color to gray
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

### show image
# color
cv.imshow("color", image)
# gray
cv.imshow("gray", gray)

cv.waitKey(0)
cv.destroyAllWindows()