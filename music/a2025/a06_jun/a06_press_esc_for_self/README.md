ffmpeg -loop 1 -i press_esc_for_self_mix.jpg -i press_esc_for_self_mix.wav -c:v libx264 -tune stillimage -c:a aac -b:a 320k -pix_fmt yuv420p -shortest press_esc_for_self.mp4

