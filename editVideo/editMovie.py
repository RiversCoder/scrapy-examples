import os
import shutil
import time
from moviepy.editor import *
import moviepy

# 存放视频的地址
BASE_URL = 'C:\\videos\\低调新说\\'
# 生成的视频地址
RENDER_URL = BASE_URL+'test\\'

class AnimalVideo:

    def __init__(self):
        pass

    def editVideo(self, path1, path2):

        # 出场动画
        start_clip = VideoFileClip("./movie/movie_start.mp4").resize(0.3333333)

        # 要播放的视频
        start_start_time = start_clip.duration
        video_clip = VideoFileClip(path1)
        video_clip = video_clip.subclip(6,10)
        video_clip = moviepy.video.fx.all.crop(video_clip, y1=65, y2=353)

        #结束动画
        end_start_time = video_clip.duration + start_start_time
        end_clip = VideoFileClip("./movie/movie_end.mp4").resize(0.3333333)

        #文字动画
        #font = "ArialUnicode"  # 只有这个支持中文
        txt_clip = TextClip("杨桃影视圈", font="./movie/movie.ttf", fontsize=19, color='white') #杨桃影视圈
        txt_clip = txt_clip.set_duration(video_clip.duration)
        video = CompositeVideoClip([#start_clip,
                                    video_clip.set_pos((0, 37)), #video_clip.set_start(start_start_time).set_pos((0, 37)),
                                    #end_clip.set_start(end_start_time),
                                    txt_clip.set_pos((8, 3))], size=start_clip.size) #set_start(start_start_time).

        #生成视频文件
        video.write_videofile(path2, fps=30, threads=1)
        #video.close()
        pass


    def cerateNewAnimalVideo(self):

        dir_list = os.listdir(BASE_URL)
        self.mkdir(RENDER_URL)

        # it = dir_list[0]
        # self.editVideo(BASE_URL+it, RENDER_URL+it)
        # time.sleep(5)
        # os.remove(BASE_URL+it)
        # time.sleep(5)
        # os.system("python editMovie.py")

        for it in dir_list:
            self.editVideo(BASE_URL+it, RENDER_URL+it)
            #time.sleep(5)
            #os.remove(BASE_URL+it)
            

    def mkdir(self, path):

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