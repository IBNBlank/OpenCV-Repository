# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-01-21 23:01:30
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-03-07 01:04:43

import cv2 as cv

file_path = "..\\example\\image\\lenacolor.png"
image = cv.imread(file_path, cv.IMREAD_UNCHANGED)

### resize
# dsize
size = (200, 100)
rows, cols = image.shape[:2]
img_dsize_1 = cv.resize(image, size)
img_dsize_2 = cv.resize(image, (round(cols*0.5), round(rows*2)))
# rate
img_rate_1 = cv.resize(image, None, fx=2, fy=1)
img_rate_2 = cv.resize(image, None, fx=1, fy=2)
img_rate_3 = cv.resize(image, None, fx=2, fy=2)

### show image
# origin
cv.imshow("origin", image)
# dsize
cv.imshow("dsize_1", img_dsize_1)
cv.imshow("dsize_2", img_dsize_2)
# rate
cv.imshow("rate_1", img_rate_1)
cv.imshow("rate_2", img_rate_2)
cv.imshow("rate_3", img_rate_3)

cv.waitKey(0)
cv.destroyAllWindows()