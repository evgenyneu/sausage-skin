ffmpeg -loop 1 -i reasonably_joyful_porcupine.jpg -i reasonably_joyful_porcupine_mix.wav -c:v libx264 -tune stillimage -c:a aac -b:a 320k -pix_fmt yuv420p -shortest reasonably_joyful_porcupine.mp4
