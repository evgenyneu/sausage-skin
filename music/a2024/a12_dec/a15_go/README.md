ffmpeg -loop 1 -i go.jpg -i go_mix.wav -c:v libx264 -tune stillimage -c:a aac -b:a 320k -pix_fmt yuv420p -shortest go.mp4

