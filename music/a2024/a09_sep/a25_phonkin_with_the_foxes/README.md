ffmpeg -loop 1 -i phonkin_with_the_foxes.jpg -i phonkin_with_the_foxes_mix_v2.wav -c:v libx264 -tune stillimage -c:a aac -b:a 320k -pix_fmt yuv420p -shortest phonkin_with_the_foxes_v2.mp4

