# 导入需要的库
from moviepy.editor import *
import moviepy
 
clip1 = VideoFileClip("test01.mp4") # add 10px contour
duration = clip1.duration
clip1 = clip1.subclip(2,duration-4)
# clip1 = clip1.fx.crop(x1=50, y1=60, x2=460, y2=275)
clip1 = moviepy.video.fx.all.crop(clip1, y1 = 56, y2 = 350) 
clip1 = moviepy.video.fx.all.crop(clip1, ) 
video = CompositeVideoClip([clip1], size=clip1.size)


# 把最后生成的视频导出到文件内
video.write_videofile("myHolidays_edited.mp4")

