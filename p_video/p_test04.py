# 导入需要的库
from moviepy.editor import *
import moviepy
import os

BASE_URL = 'C:\\videos\\低调新说\\'

class CropVideo():

    def __init__(self, path):
        self.video_dir = path
        self.rebder_md = 'render\\'
        pass

    def clipVideo(self,video_path1,video_path2): 
        clip1 = VideoFileClip(video_path1) # add 10px contour
        duration = clip1.duration
        clip1 = clip1.subclip(4,duration-8)
        clip1 = moviepy.video.fx.all.crop(clip1, y1 = 56, y2 = 350) 
        clip1 = moviepy.video.fx.all.crop(clip1, ) 
        video = CompositeVideoClip([clip1], size=clip1.size)
        # 把最后生成的视频导出到文件内
        video.write_videofile(video_path2)

    def getAllRenderVideos(self):
        files = os.listdir(self.video_dir)
        video_dir1 = BASE_URL
        video_dir2 = BASE_URL + self.rebder_md
        self.mkdir(video_dir2)
        for file in files:
            print(video_dir2+file)
            self.clipVideo(video_dir1+file, video_dir2+file)
        pass
    
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

cropvideo = CropVideo(BASE_URL)
cropvideo.getAllRenderVideos()