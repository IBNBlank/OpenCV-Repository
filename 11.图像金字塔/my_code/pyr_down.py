# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-04-28 00:07:27
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-04-28 00:10:30

import cv2 as cv
import numpy as np

file_path = "..\\example\\image\\man.bmp"
image = cv.imread(file_path, cv.IMREAD_UNCHANGED)

### pyrdown
img_down_1 = cv.pyrDown(image)
img_down_2 = cv.pyrDown(img_down_1)
img_down_3 = cv.pyrDown(img_down_2)

### show image
# origin
cv.imshow("origin", image)
# pyrdown
cv.imshow("pyrdown1", img_down_1)
cv.imshow("pyrdown2", img_down_2)
cv.imshow("pyrdown3", img_down_3)

cv.waitKey(0)
cv.destroyAllWindows()