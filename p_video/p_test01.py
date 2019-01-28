# 导入需要的库
from moviepy.editor import *
 
# 从本地载入视频myHolidays.mp4并截取00:00:50 - 00:00:60部分
clip = VideoFileClip("test01.mp4").subclip(50,60)
# watermark = (ImageClip("./logo.jpg").set_pos().set_duration(10))
watermarkVideo = VideoFileClip("test02.mp4").subclip(50,60).set_pos('right').resize(0.3)
# 调低音频音量 (volume x 0.8)
clip = clip.volumex(0.8)
clip.save_frame("frame.png", t=2)

print(clip.w) # 640
print(clip.h) # 360

 
# 做一个txt clip. 自定义样式，颜色.
txt_clip = TextClip("My Holidays 2013",fontsize=70,color='white')
 
# 文本clip在屏幕正中显示持续10秒
txt_clip = txt_clip.set_pos('center').set_duration(10)
 
# 把 text clip 的内容覆盖 video clip
video = CompositeVideoClip([clip, txt_clip,  watermarkVideo], size=clip.size)
 
# 把最后生成的视频导出到文件内
video.write_videofile("myHolidays_edited.mp4")
