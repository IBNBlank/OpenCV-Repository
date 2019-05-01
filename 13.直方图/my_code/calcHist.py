# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-04-28 17:25:58
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-04-28 17:45:48

import cv2 as cv
import matplotlib.pyplot as plt

file_path = "..\\example\\image\\girl.bmp"
image = cv.imread(file_path, cv.IMREAD_UNCHANGED)

### calculate hist
hist_blue = cv.calcHist([image], [0], None, [256], [0,255])
hist_green = cv.calcHist([image], [1], None, [256], [0,255])
hist_red = cv.calcHist([image], [2], None, [256], [0,255])
plt.plot(hist_blue, color='b')
plt.plot(hist_green, color='g')
plt.plot(hist_red, color='r')

### show image
# origin
cv.imshow("origin", image)
# plot
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()