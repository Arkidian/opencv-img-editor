import os

#文件存储path
def out_path(cnt):
    file_name = os.getcwd() + '\\static\\uploads\\' + str(int(cnt)) + '.jpg'
    return file_name

# 图片的映射：相当于图片外链
def direct_path(cnt):
    dp = 'http://127.0.0.1:5000/_uploads/photos/' + str(int(cnt)) + '.jpg'
    return dp

def file_name(cnt):
    name = str(int(cnt)) + '.jpg'
    return name

# 图片嵌入式代码：可以直接嵌入于html中
def web_path(cnt):
    website_path = '<br><img src=http://127.0.0.1:5000/_uploads/photos/' + str(int(cnt)) +'.jpg>'
    return website_path
