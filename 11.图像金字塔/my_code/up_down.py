# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-04-28 00:15:37
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-04-28 00:24:39

import cv2 as cv
import numpy as np

file_path = "..\\example\\image\\girl.bmp"
image = cv.imread(file_path, cv.IMREAD_UNCHANGED)

### pyr
# up
img_up = cv.pyrUp(image)
# down
img_down = cv.pyrDown(img_up)
# diff
img_diff = img_down - image

### show image
# origin
cv.imshow("origin", image)
# pyr
cv.imshow("up", img_up)
cv.imshow("down", img_down)
cv.imshow("diff", img_diff)

cv.waitKey(0)
cv.destroyAllWindows()