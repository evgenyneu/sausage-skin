# this will upscale the rat_race video from 768 to 2000 pixels

ffmpeg -i output_9_low.mp4 -vf scale=2000:2000 -c:a copy output_9.mp4

# Extract the last frame of the video
ffmpeg -sseof -0.1 -i output_9.mp4 -vframes 1 -q:v 2 image_9.jpg

