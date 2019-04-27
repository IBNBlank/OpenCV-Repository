# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-04-27 13:23:15
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-04-27 13:57:49

import cv2 as cv
import numpy as np

opening_file_path = "..\\example\\image\\opening.bmp"
closing_file_path = "..\\example\\image\\closing.bmp"
gradient_file_path = "..\\example\\image\\gradient.bmp"
tophat_file_path = "..\\example\\image\\tophat.bmp"
blackhat_file_path = "..\\example\\image\\blackhat.bmp"

opening_image_origin = cv.imread(opening_file_path, cv.IMREAD_UNCHANGED)
closing_image_origin = cv.imread(closing_file_path, cv.IMREAD_UNCHANGED)
gradient_image_origin = cv.imread(gradient_file_path, cv.IMREAD_UNCHANGED)
tophat_image_origin = cv.imread(tophat_file_path, cv.IMREAD_UNCHANGED)
blackhat_image_origin = cv.imread(blackhat_file_path, cv.IMREAD_UNCHANGED)

### morphology
# kernal
kernal_smaller = np.ones((3,3), np.uint8)
kernal_bigger = np.ones((10,10), np.uint8)
# opening
# img_opening = cv.morphologyEx(opening_image_origin, cv.MORPH_OPEN, kernal)
img_opening = cv.morphologyEx(opening_image_origin, cv.MORPH_OPEN, kernal_bigger)
# closing
# img_closing = cv.morphologyEx(closing_image_origin, cv.MORPH_CLOSE, kernal)
img_closing = cv.morphologyEx(closing_image_origin, cv.MORPH_CLOSE, kernal_bigger)
# gradient
# img_gradient = cv.morphologyEx(gradient_image_origin, cv.MORPH_GRADIENT, kernal)
img_gradient = cv.morphologyEx(gradient_image_origin, cv.MORPH_GRADIENT, kernal_smaller)
# tophat
img_tophat = cv.morphologyEx(tophat_image_origin, cv.MORPH_TOPHAT, kernal_bigger)
# blackhat
img_blackhat = cv.morphologyEx(blackhat_image_origin, cv.MORPH_BLACKHAT, kernal_bigger)

### show image
# origin
cv.imshow("opening origin", opening_image_origin)
cv.imshow("closing origin", closing_image_origin)
cv.imshow("gradient origin", gradient_image_origin)
cv.imshow("tophat origin", tophat_image_origin)
cv.imshow("blackhat origin", blackhat_image_origin)
# opening
cv.imshow("opening", img_opening)
# closing
cv.imshow("closing", img_closing)
# gradient
cv.imshow("gradient", img_gradient)
# tophat
cv.imshow("tophat", img_tophat)
# blackhat
cv.imshow("blackhat", img_blackhat)

cv.waitKey(0)
cv.destroyAllWindows()