import cv2
import numpy as np

from img_1_color import *
from img_2_operation import *
from img_3_transformation import *
from img_4_noise import *
from img_5_enhance import *
from img_6_morphology import *
from img_styleTransfer import *


def task(cmd, cnt):
    #     print(cmd)
    if (cmd == '10'):  # hsv_h
        color_hsv(0, cnt)
    elif (cmd == '11'):  # hsv_s
        color_hsv(1, cnt)
    elif (cmd == '12'):  # hsv_s
        color_hsv(2, cnt)
    elif (cmd == '13'):  # hsv_s
        color_rgb(0, cnt)
    elif (cmd == '14'):  # hsv_s
        color_rgb(1, cnt)
    elif (cmd == '15'):  # hsv_s
        color_rgb(2, cnt)

    elif (cmd == '20'):  # 非运算
        operate(0, cnt)
    elif (cmd == '21'):  # 或运算
        operate(1, cnt)
    elif (cmd == '22'):  # 与运算
        operate(2, cnt)
    elif (cmd == '23'):  # 加运算
        operate(3, cnt)
    elif (cmd == '24'):  # 减运算
        operate(4, cnt)
    elif (cmd == '25'):  # 乘运算
        operate(5, cnt)
    elif (cmd == '26'):  # 除运算
        operate(6, cnt)

    elif (cmd == '30'):  # 放大
        transfer(0, cnt)
    elif (cmd == '31'):  # 缩小
        transfer(1, cnt)
    elif (cmd == '32'):  # 旋转90°
        transfer(2, cnt)
    elif (cmd == '33'):  # 水平镜像
        transfer(3, cnt)
    elif (cmd == '34'):  # 垂直镜像
        transfer(4, cnt)

    elif (cmd == '40'):  # 添加噪声
        noise_add(cnt)
    elif (cmd == '41'):  # 减噪
        noise_filter(cnt)

    elif (cmd == '50'):  # 白平衡
        enhance(0, cnt)
    elif (cmd == '51'):  # 灰度世界算法
        enhance(1, cnt)
    elif (cmd == '52'):  # 直方图均衡化
        enhance(2, cnt)
    elif (cmd == '53'):  # Retinex ssr1
        enhance(3, cnt)
    elif (cmd == '54'):  # Retinex ssr2
        enhance(4, cnt)
    elif (cmd == '55'):  # Retinex msr1
        enhance(5, cnt)
    elif (cmd == '56'):  # Retinex msr2
        enhance(6, cnt)
    elif (cmd == '57'):  # Retinex msrcr
        enhance(7, cnt)
    elif (cmd == '58'):  # 自动白平衡（注：用时较长）
        enhance(8, cnt)
    elif (cmd == '59'):  # 自动色彩均衡（注：用时较长）
        enhance(9, cnt)

    elif (cmd == '60'):  # 腐蚀
        morphology(0, cnt)
    elif (cmd == '61'):  # 膨胀
        morphology(1, cnt)
    elif (cmd == '62'):  # 开运算
        morphology(2, cnt)
    elif (cmd == '63'):  # 闭运算
        morphology(3, cnt)

    # 风格迁移（注：需等待较长时间）
    elif (cmd == '70'):  # 风格：自定义
        style_transfer(0, cnt)
    elif (cmd == '71'):  # 预设风格1：starsky
        style_transfer(1, cnt)
    elif (cmd == '72'):  # 预设风格2：
        style_transfer(2, cnt)
    elif (cmd == '73'):  # 预设风格3：
        style_transfer(3, cnt)

    else:
        print('Invalid command!')
        return 1

    return 0
