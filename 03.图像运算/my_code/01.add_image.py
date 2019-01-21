# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-01-21 22:08:30
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-01-21 22:46:49

import cv2 as cv
import numpy as np

file_path = "..\\example\\image\\lena512.bmp"
image = cv.imread(file_path, cv.IMREAD_UNCHANGED)

### add
# numpy_add (sum = sum % 255)
npa = image + image
# cv_add (sum = sum if sum<=255 else 255)
cva = cv.add(image, image)

cv.imshow("Origin", image)
cv.imshow("Numpy", npa)
cv.imshow("OpenCV", cva)

cv.waitKey(0)
cv.destroyAllWindows()