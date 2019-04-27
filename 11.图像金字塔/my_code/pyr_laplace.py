# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-04-28 00:26:47
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-04-28 00:48:15

import cv2 as cv
import numpy as np

file_path = "..\\example\\image\\lena.bmp"
image = cv.imread(file_path, cv.IMREAD_UNCHANGED)

### pyr laplace
# laplace layer 0
img_down_1 = cv.pyrDown(image)
img_laplcae_0 = image - cv.pyrUp(img_down_1)
# laplace layer 1
img_down_2 = cv.pyrDown(img_down_1)
img_laplcae_1 = img_down_1 - cv.pyrUp(img_down_2)
# laplace layer 2
img_down_3 = cv.pyrDown(img_down_2)
img_laplcae_2 = img_down_2 - cv.pyrUp(img_down_3)

### recover
# img_up_3
img_up_3 = cv.pyrUp(img_down_3)
# img_up_2 = cv.pyrUp(img_down_2)
img_up_2 = cv.pyrUp(img_up_3 + img_laplcae_2)
# img_up_1 = cv.pyrUp(img_down_1)
img_up_1 = cv.pyrUp(img_up_2 + img_laplcae_1)
# img_recover = origin
img_recover = img_up_1 + img_laplcae_0
# compare
img_diff = image - img_recover

### show image
# origin
cv.imshow("origin", image)
# pyr laplace
cv.imshow("layer 0", img_laplcae_0)
cv.imshow("layer 1", img_laplcae_1)
cv.imshow("layer 2", img_laplcae_2)
# recover
cv.imshow("recover", img_recover)
cv.imshow("diff", img_diff)

cv.waitKey(0)
cv.destroyAllWindows()