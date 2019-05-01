# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-04-28 14:34:06
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-04-28 14:42:28

import cv2 as cv
import matplotlib.pyplot as plt

file_path = "..\\example\\image\\boat.jpg"
image = cv.imread(file_path, cv.IMREAD_UNCHANGED)

### hist
plt.hist(image.ravel(), 256)

### show image
# origin
cv.imshow("origin", image)
# pyplot
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()