import numpy as np
import cv2

from output import out_path

def morphology(decide,cnt):
    src = cv2.imread(out_path(cnt), cv2.IMREAD_UNCHANGED)
    if(decide==0):# 腐蚀
        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
        output = cv2.erode(src, kernel)
    elif(decide==1):# 膨胀
        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
        output = cv2.dilate(src, kernel)
    elif(decide==2):# 开运算(先腐蚀，再膨胀)
        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
        output = cv2.morphologyEx(src, cv2.MORPH_OPEN, kernel)
    elif(decide==3):# 闭运算(先膨胀，再腐蚀)
        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (10, 10))
        output = cv2.morphologyEx(src, cv2.MORPH_CLOSE, kernel)
    cv2.imwrite(out_path(cnt+1), output)