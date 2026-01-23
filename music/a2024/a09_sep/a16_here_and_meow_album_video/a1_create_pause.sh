#!/bin/bash
echo "Creating pause videos..."

# Create Pause Videos Between Tracks:
# For each pause between tracks, generate a 1-second video showing
# the previous track's image with silent audio.
for i in {1..11}; do
    ffmpeg -loop 1 -i image_${i}.jpg -f lavfi -i anullsrc=r=48000:cl=stereo \
    -t 1 -c:v libx264 -tune stillimage -pix_fmt yuv420p \
    -c:a aac -b:a 320k -movflags +faststart \
    pause_${i}.mp4
done

