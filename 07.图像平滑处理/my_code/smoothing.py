# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-04-26 14:24:08
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-04-26 14:48:19

import cv2 as cv

file_path = "..\\example\\image\\lenaNoise.png"
image = cv.imread(file_path, cv.IMREAD_UNCHANGED)

### smoothing
# mean filter
img_blur = cv.blur(image, (3,3))
# box filter
img_box = cv.boxFilter(image, -1, (3,3), normalize=0)
# gaussian filter
img_gaussian = cv.GaussianBlur(image, (3,3), 0)
# median filter
img_median = cv.medianBlur(image, 3)

### show image
# origin
cv.imshow("origin", image)
# smoothing
cv.imshow("mean filter", img_blur)
cv.imshow("box filter", img_box)
cv.imshow("gaussian filter", img_gaussian)
cv.imshow("median filter", img_median)

cv.waitKey(0)
cv.destroyAllWindows()