# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import cv2
i=cv2.imread("image\\lena256.bmp",cv2.IMREAD_UNCHANGED)
#请确保当前目录下有灰度图像lena256.bmp
'''
print(i[100,100])
i[100,100]=255
print(i[100,100])
'''
p=i[100,100]
print(p)
i[100,100]=255
p=i[100,100]
print(p)