# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-04-27 13:04:46
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-04-27 13:16:31

import cv2 as cv
import numpy as np

file_path = "..\\example\\image\\erode.bmp"
image = cv.imread(file_path, cv.IMREAD_UNCHANGED)

### erode
# kernal
kernal = np.ones((5,5), np.uint8)
# erode
img_erode_default = cv.erode(image, kernal) # The default of iterations is 1
img_erode_2 = cv.erode(image, kernal, iterations=2)
img_erode_9 = cv.erode(image, kernal, iterations=9)

### show image
# origin
cv.imshow("origin", image)
# erode
cv.imshow("default", img_erode_default)
cv.imshow("2", img_erode_2)
cv.imshow("9", img_erode_9)

cv.waitKey(0)
cv.destroyAllWindows()