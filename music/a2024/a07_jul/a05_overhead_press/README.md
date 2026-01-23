ffmpeg -loop 1 -i overhead_press_with_text.png -i overhead_press_master.wav -c:v libx264 -tune stillimage -c:a aac -b:a 320k -pix_fmt yuv420p -shortest overhead_press.mp4
