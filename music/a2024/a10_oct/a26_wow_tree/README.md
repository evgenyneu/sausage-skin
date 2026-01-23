ffmpeg -loop 1 -i wow_tree.jpg -i wow_tree_mix.wav -c:v libx264 -tune stillimage -c:a aac -b:a 320k -pix_fmt yuv420p -shortest wow_tree.mp4

