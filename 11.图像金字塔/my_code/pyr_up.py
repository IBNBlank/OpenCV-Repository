# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-04-28 00:07:52
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-04-28 00:13:33

import cv2 as cv
import numpy as np

file_path = "..\\example\\image\\lena256.bmp"
image = cv.imread(file_path, cv.IMREAD_UNCHANGED)

### pyrup
img_up_1 = cv.pyrUp(image)
img_up_2 = cv.pyrUp(img_up_1)

### show image
# origin
cv.imshow("origin", image)
# pyrup
cv.imshow("pyrup1", img_up_1)
cv.imshow("pyrup2", img_up_2)

cv.waitKey(0)
cv.destroyAllWindows()