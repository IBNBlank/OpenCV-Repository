# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-04-29 00:36:11
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-04-29 00:45:04

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

file_path = "..\\example\\image\\equ.bmp"
image = cv.imread(file_path, cv.IMREAD_GRAYSCALE)

### equalize
# equalize
img_equ = cv.equalizeHist(image)
# hist
plt.subplot(221)
plt.hist(image.ravel(), 256)
plt.subplot(222)
plt.hist(img_equ.ravel(), 256)

### show image
# origin
plt.subplot(223)
plt.imshow(image, cmap=plt.cm.gray)
plt.axis('off')
plt.subplot(224)
plt.imshow(img_equ, cmap=plt.cm.gray)
plt.axis('off')
# plot
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()