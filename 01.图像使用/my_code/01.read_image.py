# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-01-20 17:58:59
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-01-20 19:19:51

import cv2 as cv

file_path = "..\\example\\image\\test.png"

### easy read
easy_image = cv.imread(file_path)

### read with parameter
# unchanged
unchanged_image = cv.imread(file_path, cv.IMREAD_UNCHANGED)
# grayscale
grayscale_image = cv.imread(file_path, cv.IMREAD_GRAYSCALE)
# color
color_image = cv.imread(file_path, cv.IMREAD_COLOR)