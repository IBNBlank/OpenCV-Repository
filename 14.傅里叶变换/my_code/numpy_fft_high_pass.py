# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-04-30 22:51:32
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-04-30 23:28:04

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

file_path = "..\\example\\image\\lena.bmp"
image = cv.imread(file_path, cv.IMREAD_GRAYSCALE)

### fft
# fft
fft = np.fft.fft2(image)
fft_shift = np.fft.fftshift(fft)
fft_fin = 20 * np.log(np.abs(fft_shift)) # used for display
# high-pass filter
rows, cols = image.shape
crow, ccol = int(rows/2), int(cols/2)
fft_shift[crow-30:crow+30, ccol-30:ccol+30] = 0
fft_high_pass = 20 * np.log(np.abs(fft_shift)) # used for display
# ifft
ifft_shift = np.fft.ifftshift(fft_shift)
ifft_fin = np.fft.ifft2(ifft_shift)
ifft_fin = np.abs(ifft_fin)

### show image
# origin
plt.subplot(221)
plt.imshow(image, cmap=plt.cm.gray)
plt.title('origin')
plt.axis('off')
# fft
plt.subplot(222)
plt.imshow(fft_fin, cmap=plt.cm.gray)
plt.title('fft')
plt.axis('off')
# high-pass filter
plt.subplot(223)
plt.imshow(fft_high_pass, cmap=plt.cm.gray)
plt.title('high-pass filter')
plt.axis('off')
# ifft
plt.subplot(224)
plt.imshow(ifft_fin, cmap=plt.cm.gray)
plt.title('ifft')
plt.axis('off')

plt.show()
cv.waitKey(0)
cv.destroyAllWindows()