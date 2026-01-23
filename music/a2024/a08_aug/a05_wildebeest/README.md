ffmpeg -loop 1 -i wildebeest_v2.jpg -i wildebeest_mix.wav -c:v libx264 -tune stillimage -c:a aac -b:a 320k -pix_fmt yuv420p -shortest wildebeest.mp4
