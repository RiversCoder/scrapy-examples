import os
from moviepy.editor import *
import moviepy


video_clip = VideoFileClip('test.mp4').subclip(0,5)
logo_clip = ImageClip('logo2.png').resize(1/3)
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
txt_clip = TextClip("全麦馒头影视坊", font="../movie/movie.ttf", fontsize=19, color='white') # 全麦馒头影视坊
txt_clip = txt_clip.set_duration(video_clip.duration)
video = CompositeVideoClip([video_clip.set_pos((0, clip_top)),logo_clip.set_duration(video_clip.duration).set_pos((5*per, 2*per))], size=(640, 360))

video.write_videofile('test2.mp4')