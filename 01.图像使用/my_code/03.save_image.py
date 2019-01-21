# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-01-20 18:00:34
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-01-20 19:19:24

import cv2 as cv

file_path = "..\\example\\image\\test.png"
image = cv.imread(file_path)
cv.imshow("demo", image) # window_name, image_name
cv.waitKey(0)
cv.destroyAllWindows()

# save image
cv.imwrite("..\\example\\image\\test2.png", image)