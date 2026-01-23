ffmpeg -loop 1 -i household_sink_cleaner.jpg -i household_sink_cleaner_mixed.wav -c:v libx264 -tune stillimage -c:a aac -b:a 320k -pix_fmt yuv420p -shortest household_sink_cleaner.mp4
