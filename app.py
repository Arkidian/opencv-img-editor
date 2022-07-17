import os

import cv2
from flask import Flask, request
from flask_uploads import UploadSet, configure_uploads, IMAGES,\
 patch_request_class
from output import out_path
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
photo_version = 0

html = '''
    <!DOCTYPE html>
    <title>Upload File</title>
    <h1>图片上传</h1>
    <form method=post enctype=multipart/form-data>
         <input type=file name=photo>
         <input type=submit value=上传>
    </form>
    '''


# 主页面
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    del_all()
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        # app.name = filename
        app.photo_name = filename
        file_url = photos.url(filename)
        app.photo_url = file_url
        print(app.photo_name)
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


@app.route('/deal/<command_id>')
def deal(command_id):
    cnt = 0
    img = cv2.imread(photo_url)  # 根据路径读取一张图片
    cv2.imwrite(out_path(cnt), img)

    cmd = command_id

    if (cmd == 'q' or cmd == 'quit'):
        # 退出进程
        for id in range(0, cnt + 1):
            if os.path.exists(out_path(id)):
                os.remove(out_path(id))
            print('quit success')
            break

    elif (cmd == 'b' or cmd == 'back'):
        # 撤销操作
        if (cnt > 0):
            if os.path.exists(out_path(cnt)):
                os.remove(out_path(cnt))
            cnt = cnt - 1
            print('back success')

    elif (cmd == 's' or cmd == 'save'):
        # 保存操作
        cnt_max = cnt
        img = cv2.imread(out_path(cnt))
        cv2.imwrite('img_src/origin.jpg', img)
        cnt = 0
        cv2.imwrite(out_path(cnt), img)
        for id in range(1, cnt_max + 1):
            if os.path.exists(out_path(id)):
                os.remove(out_path(id))
        print('save success')

    else:
        # 图像处理操作
        success = task(cmd, cnt)
        if (success == 0):
            cnt = cnt + 1
    return "修改成功"

if __name__ == '__main__':
    app.run()