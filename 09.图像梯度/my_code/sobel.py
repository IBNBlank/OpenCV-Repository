# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-04-27 17:14:26
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-04-27 17:59:00

import cv2 as cv
import numpy as np

file_path = "..\\example\\image\\lena.bmp"
image = cv.imread(file_path, cv.IMREAD_UNCHANGED)

### sobel
# x
img_sobel_x = cv.Sobel(image, cv.CV_64F, 1, 0, ksize=3) # The default of ksize is 3
img_sobel_x = cv.convertScaleAbs(img_sobel_x) # 转回uint8
# y
img_sobel_y = cv.Sobel(image, cv.CV_64F, 0, 1)
img_sobel_y = cv.convertScaleAbs(img_sobel_y)
# xy
img_sobel_xy = cv.addWeighted(img_sobel_x, 0.5, img_sobel_y, 0.5, 0)
# xy11
img_sobel_xy11 = cv.Sobel(image, cv.CV_64F, 1, 1)
img_sobel_xy11 = cv.convertScaleAbs(img_sobel_xy11)

### show image
# origin
cv.imshow("origin", image)
# sobel
cv.imshow("x", img_sobel_x)
cv.imshow("y", img_sobel_y)
cv.imshow("xy", img_sobel_xy)
cv.imshow("xy11", img_sobel_xy11)

cv.waitKey(0)
cv.destroyAllWindows()