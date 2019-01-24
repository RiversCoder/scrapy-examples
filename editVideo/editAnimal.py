import os
from moviepy.editor import *
import moviepy


class AnimalVideo:

    def __init__(self):
        pass



    def cerateNewAnimalVideo(self):
        pass

    def editVideo(self):
        pass

    def mkdir(self, path):

        print(path)

        # 去除首位空格
        path = path.strip()
        # 去除尾部 \ 符号
        path = path.rstrip("\\")

        isExists = os.path.exists(path)

        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(path)
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            return False

animalVideo = AnimalVideo()
animalVideo.cerateNewAnimalVideo()