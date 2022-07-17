import os


def out_path(cnt):
    file_name = os.getcwd() + '\\static\\uploads\\' + str(int(cnt)) + '.jpg'
    return file_name
