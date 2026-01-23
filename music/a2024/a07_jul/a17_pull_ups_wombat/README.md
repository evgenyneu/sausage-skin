ffmpeg -loop 1 -i pull_ups_wombat.jpg -i pull_ups_wombat_mixed.wav -c:v libx264 -tune stillimage -c:a aac -b:a 320k -pix_fmt yuv420p -shortest pull_ups_aware_wombat_remix.mp4
