ffmpeg -loop 1 -i music_for_zebras.jpg -i music_for_zebras_mix.wav -c:v libx264 -tune stillimage -c:a aac -b:a 320k -pix_fmt yuv420p -shortest music_for_zebras.mp4
