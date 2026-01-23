ffmpeg -loop 1 -i cloven_hoofed.jpg -i cloven_hoofed_mix.wav -c:v libx264 -tune stillimage -c:a aac -b:a 320k -pix_fmt yuv420p -shortest cloven_hoofed.mp4

