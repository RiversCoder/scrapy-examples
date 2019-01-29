import os
from moviepy.editor import *
import moviepy

# 存放视频的地址
BASE_URL = 'D:\\videos\\videos\\mantou\\'
# 生成的视频地址
RENDER_URL = BASE_URL+'render\\'

class AnimalVideo:

    def __init__(self):
        pass

    def editVideo(self, path1, path2):

        video_clip = VideoFileClip(path1)
        logo_clip = ImageClip('./mantouVideo/logo2.png').resize(1/3)
        h = video_clip.h

        y1 = 56
        y2 = 356

        clip_y1 = h * (y1/360)
        clip_y2 = h * (y2/360)
        clip_top = h * ((y1 + 360 - y2)/2)/360
        video_clip = moviepy.video.fx.all.crop(video_clip, y1=clip_y1)

        per = h/360

        print(video_clip.size)

        #结束动画
        #end_start_time = video_clip.duration + start_start_time
        #end_clip = VideoFileClip("./animal/animal_logo_end.mp4").resize(1/3)

        #文字动画
        #font = "ArialUnicode"  # 只有这个支持中文
        # txt_clip = TextClip("全麦馒头影视坊", font="../movie/movie.ttf", fontsize=19, color='white') # 全麦馒头影视坊
        # txt_clip = txt_clip.set_duration(video_clip.duration)
        video = CompositeVideoClip([video_clip.set_pos((0, clip_top)),logo_clip.set_duration(video_clip.duration).set_pos((5*per, 2*per))], size=(640, 360))

        video.write_videofile(path2)
        pass

        #经典热门情感热门综艺，盘点情感奇葩大事件 都在这里 影视基地
        

    def cerateNewAnimalVideo(self):

        dir_list = os.listdir(BASE_URL)
        self.mkdir(RENDER_URL)
        for it in dir_list:
            self.editVideo(BASE_URL+it, RENDER_URL+it)


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

    def pr(self):
        print('123312')

animalVideo = AnimalVideo()
animalVideo.cerateNewAnimalVideo()