ffmpeg -loop 1 -i regular_anomaly.jpg -i regular_anomaly_mix.wav -c:v libx264 -tune stillimage -c:a aac -b:a 320k -pix_fmt yuv420p -shortest regular_anomaly.mp4
