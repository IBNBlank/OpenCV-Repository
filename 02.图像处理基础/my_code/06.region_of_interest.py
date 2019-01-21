# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-01-20 23:24:02
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-01-20 23:43:29

import cv2 as cv
import numpy as np

file_path_1 = "..\\example\\image\\lenacolor.png"
image_1 = cv.imread(file_path_1, cv.IMREAD_UNCHANGED)

file_path_2 = "..\\example\\image\\girl.bmp"
image_2 = cv.imread(file_path_2, cv.IMREAD_UNCHANGED)

### region of interest (face)
face = np.ones((180,100,3))
face = image_1[220:400, 250:350]
# show face
cv.imshow("face", face)
# copy in origin image
image_1[0:180, 0:100] = face
cv.imshow("copy_1", image_1)
# copy in another image
image_2[0:180, 0:100] = face
cv.imshow("copy_2", image_2)

cv.waitKey(0)
cv.destroyAllWindows()