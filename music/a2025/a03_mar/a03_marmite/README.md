ffmpeg -loop 1 -i hi_this_is_our_cat_marmite_cover.jpg -i hi_this_is_our_cat_marmite.wav -c:v libx264 -tune stillimage -c:a aac -b:a 320k -pix_fmt yuv420p -shortest hi_this_is_our_cat_marmite.mp4

