import os

import cv2
from flask import Flask, request
from flask_uploads import UploadSet, configure_uploads, IMAGES,\
 patch_request_class
from output import out_path , web_path
from program import task

app = Flask(__name__)
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '\\static\\uploads'  # 文件储存地址

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # 文件大小限制，默认为16MB

# 存储的最开始的图片的名字 后面上传就会改变
photo_name = 'Tsunami_by_hokusai_19th_century.jpg'
photo_url =os.getcwd() + '\\static\\uploads\\' + 'Tsunami_by_hokusai_19th_century.jpg'
# 现在的图片的版本
app.config['cnt'] = 0

html = '''
    <!DOCTYPE html>
    <title>Upload File</title>
    <h1>图片上传</h1>
    <form method=post enctype=multipart/form-data>
         <input type=file name=photo>
         <input type=submit value=上传>
    </form>
    '''

pure_html = '''
	<!DOCTYPE html>
	<title>Processed Image</title>
	'''

# 主页面
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    cnt = 0
    del_all()
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        # app.name = filename
        app.photo_name = filename
        file_url = photos.url(filename)
        app.photo_url = file_url
        img = cv2.imread(photo_url)  # 根据路径读取一张图片
        cv2.imwrite(out_path(0), img)
        print(file_url)
        return html + '<br><img src=' + file_url + '>'
    return html


# 删除uploads文件夹
@app.route('/delete_all')
def del_all():
    ls = os.listdir(app.config['UPLOADED_PHOTOS_DEST'])
    for i in ls:
        c_path = os.path.join(app.config['UPLOADED_PHOTOS_DEST'], i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)


@app.route('/delete_file')
def del_file(path):
    if os.path.exists(path):
        os.remove(path)


# 通过commmand_id来选择处理的方式，commmand_id具体内容再program.py里面找
@app.route('/deal/<command_id>')
def deal(command_id):
    img = cv2.imread(photo_url)  # 根据路径读取一张图片

    cmd = command_id

    if (cmd == 'b' or cmd == 'back'):
        # 撤销操作
        if (app.config['cnt'] > 0):
            if os.path.exists(out_path(app.config['cnt'])):
                os.remove(out_path(app.config['cnt']))
            app.config['cnt'] = app.config['cnt'] - 1
            print('back success')

    elif (cmd == 's' or cmd == 'save'):
        # 保存操作
        cnt_max = app.config['cnt']
        img = cv2.imread(out_path(app.config['cnt']))
        cv2.imwrite(os.getcwd() + '\\static', img)
        cnt = 0
        cv2.imwrite(out_path(cnt), img)
        for id in range(1, cnt_max + 1):
            if os.path.exists(out_path(id)):
                os.remove(out_path(id))
        print('save success')

    else:
        # 图像处理操作
        success = task(cmd, app.config['cnt'])
        if (success == 0):
            app.config['cnt'] = app.config['cnt'] + 1
        str_cnt = str(app.config['cnt'])
        print(type(str_cnt))
        print(app.config['cnt'])
    return pure_html + web_path(app.config['cnt'])

if __name__ == '__main__':
    app.run()