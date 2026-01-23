ffmpeg -loop 1 -i kitten_3_mix.jpg -i kitten_3_mix_v2.wav -c:v libx264 -tune stillimage -c:a aac -b:a 320k -pix_fmt yuv420p -shortest kitten_3.mp4

