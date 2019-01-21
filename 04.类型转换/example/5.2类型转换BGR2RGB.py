# -*- coding: utf-8 -*-
import cv2
a=cv2.imread("image\\lenacolor.png")
b=cv2.cvtColor(a,cv2.COLOR_BGR2RGB)
cv2.imshow("BGR",a)
cv2.imshow("RGB",b)
cv2.waitKey()
cv2.destroyAllWindows()
