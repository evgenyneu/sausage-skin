ffmpeg -loop 1 -i spaghetti_night.jpg -i spaghetti_night_version_two_mixed.wav -c:v libx264 -tune stillimage -c:a aac -b:a 320k -pix_fmt yuv420p -shortest spaghetti_night_v2.mp4

