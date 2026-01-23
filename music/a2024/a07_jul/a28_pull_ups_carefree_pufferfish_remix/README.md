ffmpeg -loop 1 -i pufferfish.jpg -i pull_ups_carefree_pufferfish_remix_mixed.wav -c:v libx264 -tune stillimage -c:a aac -b:a 320k -pix_fmt yuv420p -shortest pull_ups_carefree_pufferfish_remix.mp4
