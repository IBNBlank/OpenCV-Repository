# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-04-30 23:29:07
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-04-30 23:59:16

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

file_path = "..\\example\\image\\lena.bmp"
image = cv.imread(file_path, cv.IMREAD_GRAYSCALE)

### dft
# dft
dft = cv.dft(np.float32(image), flags=cv.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
dft_fin = 20 * np.log(cv.magnitude(dft_shift[:,:,0], dft_shift[:,:,1])) # used for display
# low-pass filter
rows, cols = image.shape
crow, ccol = int(rows/2), int(cols/2)
mask = np.zeros((rows,cols,2), np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] = 1
dft_shift *= mask
dft_low_pass = 20 * np.log(cv.magnitude(dft_shift[:,:,0], dft_shift[:,:,1])) # used for display
# idft
idft_shift = np.fft.ifftshift(dft_shift)
idft_fin = cv.idft(idft_shift)
idft_fin = cv.magnitude(idft_fin[:,:,0], idft_fin[:,:,1])

### show image
# origin
plt.subplot(221)
plt.imshow(image, cmap=plt.cm.gray)
plt.title('origin')
plt.axis('off')
# dft
plt.subplot(222)
plt.imshow(dft_fin, cmap=plt.cm.gray)
plt.title('dft')
plt.axis('off')
# low-pass filter
plt.subplot(223)
plt.imshow(dft_low_pass, cmap=plt.cm.gray)
plt.title('low-pass filter')
plt.axis('off')
# ifft
plt.subplot(224)
plt.imshow(idft_fin, cmap=plt.cm.gray)
plt.title('idft')
plt.axis('off')

plt.show()
cv.waitKey(0)
cv.destroyAllWindows()