# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-01-20 17:59:20
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-01-20 23:59:54

import cv2 as cv

file_path = "..\\example\\image\\test.png"
image = cv.imread(file_path)

### show image
cv.imshow("demo", image) # window_name, image_name

### delay
delay = 0     # wait all the time
# delay = 1000  # wait 1 sec
# delay = -1    # wait for keyboard
cv.waitKey(delay)

### destory (delect from memory)
cv.destroyAllWindows()