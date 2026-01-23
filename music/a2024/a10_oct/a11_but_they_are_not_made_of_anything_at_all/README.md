ffmpeg -loop 1 -i but_they_are_not_made_of_anything_at_all2.jpg -i but_they_are_not_made_of_anything_at_all_mix2.wav -c:v libx264 -tune stillimage -c:a aac -b:a 320k -pix_fmt yuv420p -shortest but_they_are_not_made_of_anything_at_all2.mp4

