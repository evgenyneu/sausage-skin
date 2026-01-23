ffmpeg -loop 1 -i everything_appears_on_its_own.jpg -i everything_appears_on_its_own_mix.wav -c:v libx264 -tune stillimage -c:a aac -b:a 320k -pix_fmt yuv420p -shortest everything_appears_on_its_own.mp4

