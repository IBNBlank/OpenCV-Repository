# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-04-26 13:55:17
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-04-26 14:21:41

import cv2 as cv

file_path = "..\\example\\image\\lena512.bmp"
image = cv.imread(file_path, cv.IMREAD_UNCHANGED)

### threshold
# binary
retval, img_binary = cv.threshold(image, 127, 255, cv.THRESH_BINARY)
# binary inverted
retval, img_binary_inverted = cv.threshold(image, 127, 255, cv.THRESH_BINARY_INV)
# truncate
retval, img_truncate = cv.threshold(image, 127, 255, cv.THRESH_TRUNC)
# threshold to zero
retval, img_threshold_to_zero = cv.threshold(image, 127, 255, cv.THRESH_TOZERO)
# threshold to zero inverted
retval, img_threshold_to_zero_inverted = cv.threshold(image, 127, 255, cv.THRESH_TOZERO_INV)

### show image
# origin
cv.imshow("origin", image)
# threshold
cv.imshow("binary", img_binary)
cv.imshow("binary inverted", img_binary_inverted)
cv.imshow("truncate", img_truncate)
cv.imshow("threshold to zero", img_threshold_to_zero)
cv.imshow("threshold to zero inverted", img_threshold_to_zero_inverted)

cv.waitKey(0)
cv.destroyAllWindows()