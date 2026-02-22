ffmpeg -loop 1 -i ur_best_is_enouph_2000.jpg -i ur_best_is_enouph_mix.wav -c:v libx264 -tune stillimage -c:a aac -b:a 320k -pix_fmt yuv420p -shortest ur_best_is_enouph_2000.mp4
