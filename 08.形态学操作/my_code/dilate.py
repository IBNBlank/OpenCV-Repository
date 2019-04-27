# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-04-27 13:19:52
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-04-27 13:21:56

import cv2 as cv
import numpy as np

file_path = "..\\example\\image\\dilation.bmp"
image = cv.imread(file_path, cv.IMREAD_UNCHANGED)

### dilate
# kernal
kernal = np.ones((5,5), np.uint8)
# dilate
img_dilate_default = cv.dilate(image, kernal) # The default of iterations is 1
img_dilate_2 = cv.dilate(image, kernal, iterations=2)
img_dilate_9 = cv.dilate(image, kernal, iterations=9)

### show image
# origin
cv.imshow("origin", image)
# dilate
cv.imshow("default", img_dilate_default)
cv.imshow("2", img_dilate_2)
cv.imshow("9", img_dilate_9)

cv.waitKey(0)
cv.destroyAllWindows()