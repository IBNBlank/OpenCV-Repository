# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-01-21 23:00:50
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-01-21 23:11:04

import cv2 as cv

file_path = "..\\example\\image\\lenacolor.png"
image = cv.imread(file_path, cv.IMREAD_UNCHANGED)

### BGR to RGB
rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)

### show image
# bgr
cv.imshow("BGR", image)
# rgb
cv.imshow("RGB", rgb)

cv.waitKey(0)
cv.destroyAllWindows()