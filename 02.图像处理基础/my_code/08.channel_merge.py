# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-01-20 23:49:34
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-01-21 00:35:44

import cv2 as cv
import numpy as np

file_path = "..\\example\\image\\lenacolor.png"
image = cv.imread(file_path, cv.IMREAD_UNCHANGED)
blue, green, red = cv.split(image)

### merge
# merge in wrong orders
brg = cv.merge([blue, red, green])
grb = cv.merge([green, red, blue])
gbr = cv.merge([green, blue, red])
rgb = cv.merge([red, green, blue])
rbg = cv.merge([red, blue, green])
# show
cv.imshow("origin", image)
cv.imshow("BRG", brg)
cv.imshow("GRB", grb)
cv.imshow("GBR", gbr)
cv.imshow("RGB", rgb)
cv.imshow("RBG", rbg)

cv.waitKey(0)
cv.destroyAllWindows()