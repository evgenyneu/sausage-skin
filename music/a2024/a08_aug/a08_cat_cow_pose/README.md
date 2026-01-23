ffmpeg -loop 1 -i cat_cow_pose.jpg -i cat_cow_pose_mix.wav -c:v libx264 -tune stillimage -c:a aac -b:a 320k -pix_fmt yuv420p -shortest cat_cow_pose.mp4
