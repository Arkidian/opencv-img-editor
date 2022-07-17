import numpy as np
import cv2

from output import out_path

def transfer(decide,cnt):
    img = cv2.imread(out_path(cnt))
    height, width, channel = img.shape
    if(decide==0):# 放大
        img = cv2.resize(img, (0, 0), fx=1.1, fy=1.1, interpolation=cv2.INTER_LINEAR)
    elif(decide==1):# 缩小
        img = cv2.resize(img, (0, 0), fx=0.9, fy=0.9, interpolation=cv2.INTER_LINEAR)
    elif(decide==2):# 旋转90°
        img = cv2.resize(img, (width, width))
        M = cv2.getRotationMatrix2D((width / 2, width / 2), 90, 1)
        img = cv2.warpAffine(img, M, (width, width))
        img = cv2.resize(img, (height, width))
    elif(decide==3):# 水平镜像
        img = cv2.flip(img,1,dst=None)
    elif(decide==4):# 垂直镜像
        img = cv2.flip(img,0,dst=None) 
    cv2.imwrite(out_path(cnt+1), img)