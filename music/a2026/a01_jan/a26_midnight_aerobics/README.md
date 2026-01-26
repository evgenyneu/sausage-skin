ffmpeg -loop 1 -i mighnight_aerobics_cover.jpg -i midnight_aerobics_mix.wav -c:v libx264 -tune stillimage -c:a aac -b:a 320k -pix_fmt yuv420p -shortest midnight_aerobics_mix.mp4
