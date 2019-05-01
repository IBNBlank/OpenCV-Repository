# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-04-29 00:45:48
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-04-29 00:50:45

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

file_path = "..\\example\\image\\girl.bmp"
gray_image = cv.imread(file_path, cv.IMREAD_GRAYSCALE)
color_image = cv.imread(file_path, cv.IMREAD_UNCHANGED)

### show image
# gray
plt.subplot(121)
plt.imshow(gray_image, cmap=plt.cm.gray)
plt.axis('off')
# color
b, g, r = cv.split(color_image)
color_image = cv.merge([r,g,b])
plt.subplot(122)
plt.imshow(color_image)
plt.axis('off')
# plot
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()