import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

from PIL import Image
import matplotlib.pyplot as plt

import torchvision.transforms as transforms
import torchvision.models as models
from torchvision.utils import save_image

from utils import *
from models import *

import numpy as np
import os
from output import out_path
# %matplotlib inline
# %config InlineBackend.figure_format = 'retina'


def style_transfer(decide,cnt):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    set_style(decide)
    de_resize(cnt)
    width = 512
    style_img = read_image('../img_src/style.jpg', target_width=width).to(device)
    content_img = read_image(out_path(cnt), target_width=width).to(device)
#     plt.figure(figsize=(12, 6))

#     plt.subplot(1, 2, 1)
#     imshow(style_img, title='Style Image')
#     plt.subplot(1, 2, 2)
#     imshow(content_img, title='Content Image')

    vgg16 = models.vgg16(pretrained=True)
    vgg16 = VGG(vgg16.features[:23]).to(device).eval()
    
    style_features = vgg16(style_img)
    content_features = vgg16(content_img)
    
    [x.shape for x in content_features]
    
    def gram_matrix(y):
        (b, ch, h, w) = y.size()
        features = y.view(b, ch, w * h)
        features_t = features.transpose(1, 2)
        gram = features.bmm(features_t) / (ch * h * w)
        return gram
    
    style_grams = [gram_matrix(x) for x in style_features]
    [x.shape for x in style_grams]
    
    input_img = content_img.clone()
    optimizer = optim.LBFGS([input_img.requires_grad_()])
    style_weight = 1e7
    content_weight = 1
    
    run = [0]
    while run[0] <= 300:
        def f():
            optimizer.zero_grad()
            features = vgg16(input_img)
            
            content_loss = F.mse_loss(features[2], content_features[2]) * content_weight
            style_loss = 0
            grams = [gram_matrix(x) for x in features]
            for a, b in zip(grams, style_grams):
                style_loss += F.mse_loss(a, b) * style_weight
            
            loss = style_loss + content_loss
            
            if run[0] % 10 == 0:
                print('Step {}: Style Loss: {:4f} Content Loss: {:4f}'.format(
                    int(run[0]/10), style_loss.item()/style_weight, content_loss.item()/content_weight))
            run[0] += 1
            
            loss.backward()
            return loss
        
        optimizer.step(f)
        
    plt.figure(figsize=(18, 6))
    
    plt.subplot(1, 3, 1)
    imshow(style_img, title='Style Image')
    
    plt.subplot(1, 3, 2)
    imshow(content_img, title='Content Image')
    
    plt.subplot(1, 3, 3)
    imshow(input_img, title='Output Image')
    plt.savefig('../img_src/transfer.jpg')
    
    plt.figure(figsize=(8, 8))
    plt.subplot(1, 1, 1)
    plt.axis('off')
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(0, 0)
    imshow(input_img)
    plt.savefig(out_path(cnt+1))

def de_resize(cnt):
    img = cv2.imread(out_path(cnt))
    img = cv2.resize(img, (612, 612), interpolation=cv2.INTER_LINEAR)
    cv2.imwrite(out_path(cnt), img)
    img = cv2.imread('../img_src/style.jpg')
    img = cv2.resize(img, (612, 612), interpolation=cv2.INTER_LINEAR)
    cv2.imwrite('../img_src/style.jpg', img)
    
def set_style(decide):
    file_name = '../img_src/styles/style'+ str(int(decide)) +'.jpg'
    if os.path.exists(file_name):
        img = cv2.imread(file_name)
        cv2.imwrite('../img_src/style.jpg', img)