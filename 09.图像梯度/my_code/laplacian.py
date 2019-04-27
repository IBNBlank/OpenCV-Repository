# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-04-27 17:54:02
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-04-27 17:58:43

import cv2 as cv
import numpy as np

file_path = "..\\example\\image\\lena.bmp"
image = cv.imread(file_path, cv.IMREAD_UNCHANGED)

### laplacian
img_laplacian = cv.Laplacian(image, cv.CV_64F)
img_laplacian = cv.convertScaleAbs(img_laplacian) # 转回uint8

### show image
# origin
cv.imshow("origin", image)
# laplacian
cv.imshow("laplacian", img_laplacian)

cv.waitKey(0)
cv.destroyAllWindows()