ffmpeg -loop 1 -i pull_ups.png -i pull_ups_master.wav -c:v libx264 -tune stillimage -c:a aac -b:a 320k -pix_fmt yuv420p -shortest pull_ups.mp4
