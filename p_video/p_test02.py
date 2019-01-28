# 导入需要的库
from moviepy.editor import *
 
clip1 = VideoFileClip("test01.mp4").margin(10).subclip(50,60) # add 10px contour
clip2 = clip1.fx( vfx.mirror_x)
clip3 = clip1.fx( vfx.mirror_y)
clip4 = clip1.resize(0.60) # downsize 60%
final_clip = clips_array([[clip1, clip2],
                          [clip3, clip4]])
final_clip.resize(width=480).write_videofile("my_stack.mp4")
