#!/bin/bash
echo "Converting MOV files to MP4 format..."

echo "Combining videos into one..."
# Use concat demuxer with constant frame rate mode
ffmpeg -f concat -safe 0 -i inputs.txt \
    -c:v libx264 -preset medium -crf 18 \
    -c:a aac -b:a 320k -pix_fmt yuv420p \
    -vsync cfr -r 25 \
    "album_combined.mp4"

echo "Videos combined successfully into album_combined.mp4"
