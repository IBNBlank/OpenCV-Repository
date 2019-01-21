# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-01-21 22:47:28
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-01-21 22:54:12

import cv2 as cv
import numpy as np

lena_path = "..\\example\\image\\lena.bmp"
lena = cv.imread(lena_path, cv.IMREAD_UNCHANGED)

boat_path = "..\\example\\image\\boat.bmp"
boat = cv.imread(boat_path, cv.IMREAD_UNCHANGED)

### add weighted
alpha = 0.6
beta = 0.3
gamma = 0
result = cv.addWeighted(lena, alpha, boat, beta, gamma)

cv.imshow("lena", lena)
cv.imshow("boat", boat)
cv.imshow("addWeighted", result)

cv.waitKey(0)
cv.destroyAllWindows()