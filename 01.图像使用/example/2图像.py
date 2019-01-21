# -*- coding: utf-8 -*-
import cv2
i=cv2.imread("E:\\lesson\\image\\test.png")
cv2.imshow("Demo",i)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("E:\\lesson\\image\\lesson1.png",i)