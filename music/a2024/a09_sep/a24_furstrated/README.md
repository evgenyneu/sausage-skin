ffmpeg -loop 1 -i no_reason_to_grow_furstrated.jpg -i no_reason_to_grow_furstrated_mix.wav -c:v libx264 -tune stillimage -c:a aac -b:a 320k -pix_fmt yuv420p -shortest no_reason_to_grow_furstrated.mp4

