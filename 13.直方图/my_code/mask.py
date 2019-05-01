# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-04-28 18:45:10
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-04-28 18:55:51

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

file_path = "..\\example\\image\\boat.bmp"
image = cv.imread(file_path, cv.IMREAD_UNCHANGED)

### calculate hist
# mask
mask = np.zeros(image.shape, np.uint8)
mask[200:400, 200:400] = 255
img_mask = cv.bitwise_and(image, mask)
# hist
hist = cv.calcHist([image], [0], None, [256], [0,255])
hist_mask = cv.calcHist([image], [0], mask, [256], [0,255])
plt.plot(hist, color='b')
plt.plot(hist_mask, color='r')

### show image
# origin
cv.imshow("origin", image)
cv.imshow("mask", mask)
cv.imshow("mask image", img_mask)
# plot
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()