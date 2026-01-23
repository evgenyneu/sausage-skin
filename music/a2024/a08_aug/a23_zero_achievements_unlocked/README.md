ffmpeg -loop 1 -i zero_achievements_unlocked.jpg -i zero_achievements_unlocked_mix.wav -c:v libx264 -tune stillimage -c:a aac -b:a 320k -pix_fmt yuv420p -shortest zero_achievements_unlocked.mp4
