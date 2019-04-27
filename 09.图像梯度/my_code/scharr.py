# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-04-27 17:39:17
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-04-27 17:58:51

import cv2 as cv
import numpy as np

file_path = "..\\example\\image\\lena.bmp"
image = cv.imread(file_path, cv.IMREAD_UNCHANGED)

### scharr
# x
img_scharr_x = cv.Scharr(image, cv.CV_64F, 1, 0) # The default of ksize is 3
img_scharr_x = cv.convertScaleAbs(img_scharr_x) # 转回uint8
# y
img_scharr_y = cv.Scharr(image, cv.CV_64F, 0, 1)
img_scharr_y = cv.convertScaleAbs(img_scharr_y)
# xy
img_scharr_xy = cv.addWeighted(img_scharr_x, 0.5, img_scharr_y, 0.5, 0)

### show image
# origin
cv.imshow("origin", image)
# scharr
cv.imshow("x", img_scharr_x)
cv.imshow("y", img_scharr_y)
cv.imshow("xy", img_scharr_xy)

cv.waitKey(0)
cv.destroyAllWindows()