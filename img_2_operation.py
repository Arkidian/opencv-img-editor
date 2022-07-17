import numpy as np
import cv2

from output import out_path

def operate(decide,cnt):
    X = cv2.imread(out_path(cnt))
    height, width, channel = X.shape
    if(decide==0):#非
        X = ~X
    else:
        Y = cv2.imread('../img_src/operate.jpg')
        Y = cv2.resize(Y, (width, height), interpolation=cv2.INTER_LINEAR)
        if(decide==1):#或
            X = X | Y
        elif(decide==2):#与
            X = X & Y
        elif(decide==3):#加
            X = cv2.add(X, Y)
        elif(decide==4):#减
            X = cv2.subtract(X, Y)
        elif(decide==5):#乘
            X = cv2.multiply(X, Y)
        elif(decide==6):#除
            X = cv2.divide(X, Y)
            
    cv2.imwrite(out_path(cnt+1), X)