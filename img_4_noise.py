import numpy as np
import cv2
import random

from output import out_path

def noise_add(cnt):# 添加噪声
    image = cv2.imread(out_path(cnt))
    output = np.zeros(image.shape,np.uint8) 
    prob = 0.01 
    for i in range(image.shape[0]):  
        for j in range(image.shape[1]):  
            rdn = random.random()  
            if rdn < prob:   
                output[i][j] = random.randint(0,255) 
            else:   
                output[i][j] = image[i][j] 
    cv2.imwrite(out_path(cnt+1), output)
    
def noise_filter(cnt):# 减噪（使用中值滤波）
    image = cv2.imread(out_path(cnt))
    output = cv2.medianBlur(src=image, ksize=3)
    cv2.imwrite(out_path(cnt+1), output)
    