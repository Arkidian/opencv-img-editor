import cv2
import numpy as np
import os

from program import out_path,task

if __name__ == '__main__':
    for id in range(1,1000):
        if os.path.exists(out_path(id)):
            os.remove(out_path(id))
    cnt = 0;
    img = cv2.imread('../img_src/origin.jpg') # 根据路径读取一张图片
    cv2.imwrite(out_path(cnt),img)
    while(1):
        cmd = input("cmd: ")
        
        if(cmd=='q' or cmd=='quit'):
            # 退出进程
            for id in range(0,cnt+1):
                if os.path.exists(out_path(id)):
                    os.remove(out_path(id))
            print('quit success')
            break
            
        elif(cmd=='b' or cmd=='back'):
            # 撤销操作
            if(cnt>0):
                if os.path.exists(out_path(cnt)):
                    os.remove(out_path(cnt))
                cnt=cnt-1
                print('back success')
                
        elif(cmd=='s' or cmd=='save'):
            # 保存操作
            cnt_max=cnt
            img = cv2.imread(out_path(cnt))
            cv2.imwrite('img_src/origin.jpg',img)
            cnt=0
            cv2.imwrite(out_path(cnt),img)
            for id in range(1,cnt_max+1):
                if os.path.exists(out_path(id)):
                    os.remove(out_path(id))
            print('save success')
            
        else:    
            # 图像处理操作
            success=task(cmd,cnt)
            if(success==0):
                cnt=cnt+1