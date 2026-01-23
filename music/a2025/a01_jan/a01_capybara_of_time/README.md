ffmpeg -loop 1 -i capybara_of_time.jpg -i capybara_of_time_mix.wav -c:v libx264 -tune stillimage -c:a aac -b:a 320k -pix_fmt yuv420p -shortest capybara_of_time.mp4

