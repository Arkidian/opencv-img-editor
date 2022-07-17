import cv2
import numpy as np

from output import out_path

# decide: 0->h, 1->s, 2->v
def color_hsv(decide,cnt):
    img = cv2.imread(out_path(cnt)) # 根据路径读取一张图片
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  
#     h = hsv[:,:,0]  
#     s = hsv[:,:,1]  
#     v = hsv[:,:,2]
    output = cv2.cvtColor(hsv[:,:,decide], cv2.COLOR_GRAY2RGB)
    cv2.imwrite(out_path(cnt+1),output)
    
# decide: 0->b, 1->g, 2->r
def color_rgb(decide,cnt):
    img = cv2.imread(out_path(cnt)) # 根据路径读取一张图片
#     b = img[:, :, 0]  
#     g = img[:, :, 1]  
#     r = img[:, :, 2]  
    output = cv2.cvtColor(img[:,:,decide], cv2.COLOR_GRAY2RGB)
    cv2.imwrite(out_path(cnt+1),output)