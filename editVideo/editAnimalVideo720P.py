import os
from moviepy.editor import *
import moviepy

# 存放视频的地址
BASE_URL = 'D:\\videos\\youtube动物\\01.28\\'
# 生成的视频地址
RENDER_URL = BASE_URL+'render\\'

class AnimalVideo:

    def __init__(self):
        pass

    def editVideo(self, path1, path2):

        # 出场动画
        start_clip = VideoFileClip("./animal/animal_logo_start.mp4").resize(2 / 3)

        # 要播放的视频
        start_start_time = start_clip.duration
        video_clip = VideoFileClip(path1)
        video_clip = video_clip.subclip(0, video_clip.duration-10 )
        #video_clip = moviepy.video.fx.all.crop(video_clip, y1=56, y2=352)

        #结束动画
        end_start_time = video_clip.duration + start_start_time
        end_clip = VideoFileClip("./animal/animal_logo_end.mp4").resize(2 / 3)

        #文字动画
        #font = "ArialUnicode"  # 只有这个支持中文
        txt_clip = TextClip("萌宠影视汇", font="./movie/movie.ttf", fontsize=19, color='white') # 萌宠影视汇
        txt_clip = txt_clip.set_duration(video_clip.duration)
        video = CompositeVideoClip([start_clip,
                                    video_clip.set_start(start_start_time),
                                    end_clip.set_start(end_start_time),
                                    txt_clip.set_start(start_start_time).set_pos((10, 10))], size=start_clip.size)
        #生成视频文件
        video.write_videofile(path2)
        pass


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