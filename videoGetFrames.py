from moviepy.editor import VideoFileClip
import numpy as np
import os
from datetime import datetime
from PIL import Image
import cv2

videoF = VideoFileClip("file.avi")
os.makedirs("frames", exist_ok=True)
\
# if files exist, delete them~
if os.listdir("frames"):
    for f in os.listdir("frames"):
        os.remove(os.path.join("frames", f))

if os.path.exists("out.mp4"):
    os.remove("out.mp4")
# get the duration of the video and the frame rate
duration = videoF.duration
fps = videoF.fps

# calculate the number of frames
numFrames = int(duration * fps)

# get every frame and save it as a numpy array 
for i in range(numFrames):
    frame = videoF.get_frame(i/fps)
    #for each frame draw a circle that goes from 160 to 320 according to a sine function
    frame = cv2.circle(frame, (round(240 + 80 * np.sin(i/fps)), round(135 + 90 * np.cos(i/fps))), int(50), (0, 0, 255), -1)
    #save the frame as a png file
    Image.fromarray(frame).save(os.path.join("frames", "frame" + str(i) + ".png"))

# create a video from the frames
os.system("ffmpeg -r " + str(fps) + " -i frames/frame%d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p out.mp4")


