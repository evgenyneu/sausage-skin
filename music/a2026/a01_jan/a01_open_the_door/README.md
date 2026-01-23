ffmpeg -loop 1 -i open_the_door_2000.jpg -i open_the_door_mix.wav -c:v libx264 -tune stillimage -c:a aac -b:a 320k -pix_fmt yuv420p -shortest open_the_door_mix.mp4

