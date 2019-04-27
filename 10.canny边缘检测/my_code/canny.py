# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-04-27 18:01:16
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-04-27 18:13:19

import cv2 as cv
import numpy as np

file_path = "..\\example\\image\\lena.bmp"
image = cv.imread(file_path, cv.IMREAD_UNCHANGED)

### canny
img_canny_1 = cv.Canny(image, 100, 200) # image, minVal, maxVal
img_canny_2 = cv.Canny(image, 64, 128) # image, minVal, maxVal

### show image
# origin
cv.imshow("origin", image)
# canny
cv.imshow("canny1", img_canny_1)
cv.imshow("canny2", img_canny_2)

cv.waitKey(0)
cv.destroyAllWindows()