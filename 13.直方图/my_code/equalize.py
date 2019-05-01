# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-04-28 21:38:05
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-04-28 21:57:25

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

file_path = "..\\example\\image\\equ.bmp"
image = cv.imread(file_path, cv.IMREAD_GRAYSCALE)

### equalize
# equalize
img_equ = cv.equalizeHist(image)
# hist
hist_origin = cv.calcHist([image], [0], None, [256], [0,255])
hist_equal = cv.calcHist([img_equ], [0], None, [256], [0,255])
plt.plot(hist_origin, color='b')
plt.plot(hist_equal, color='r')

### show image
# origin
cv.imshow("origin", image)
cv.imshow("equal", img_equ)
# plot
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()