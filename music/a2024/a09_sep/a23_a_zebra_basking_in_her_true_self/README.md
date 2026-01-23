ffmpeg -loop 1 -i a_zebra_basking_in_her_true_self.jpg -i a_zebra_basking_in_her_true_self_mix.wav -c:v libx264 -tune stillimage -c:a aac -b:a 320k -pix_fmt yuv420p -shortest -metadata:s:a ISRC=AUQ1W2400012 a_zebra_basking_in_her_true_self_isrc2.mp4

# Check audio metadata
ffprobe -v quiet -show_entries stream=index:stream_tags a_zebra_basking_in_her_true_self_isrc2.mp4


