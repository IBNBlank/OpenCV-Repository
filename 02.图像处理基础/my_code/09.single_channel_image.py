# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-01-21 00:13:17
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-01-21 00:36:13

import cv2 as cv
import numpy as np

file_path = "..\\example\\image\\lenacolor.png"
image = cv.imread(file_path, cv.IMREAD_UNCHANGED)
blue, green, red = cv.split(image)

rows, cols, chn = image.shape
zero_channel = np.zeros((rows,cols), dtype=image.dtype)
full_channel = np.full((rows,cols), 255, dtype=image.dtype)

### merge
# merge with zeros or 255s
bz = cv.merge([blue, zero_channel, zero_channel])
gz = cv.merge([zero_channel, green, zero_channel])
rz = cv.merge([zero_channel, zero_channel, red])
bf = cv.merge([blue, full_channel, full_channel])
gf = cv.merge([full_channel, green, full_channel])
rf = cv.merge([full_channel, full_channel, red])
# show
cv.imshow("origin", image)
cv.imshow("BZero", bz)
cv.imshow("GZero", gz)
cv.imshow("RZero", rz)
cv.imshow("BFull", bf)
cv.imshow("GFull", gf)
cv.imshow("RFull", rf)

cv.waitKey(0)
cv.destroyAllWindows()