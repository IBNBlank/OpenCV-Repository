# -*- coding: utf-8 -*-
import cv2
i=cv2.imread("e:\\lesson\\image\\lenacolor.png",cv2.IMREAD_UNCHANGED)
#请确保在指定目录下有彩色图像文件
print(i[100,100])
i[100,100,0]=255
print(i[100,100])



'''
同时更改三个通道
print(i[100,100])
i[100,100]=[255,255,255]
print(i[100,100])
'''


'''
更改一个像素块
cv2.imshow("original",i)
i[100:150,100:150]=[0,0,255]
cv2.imshow("result",i)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''