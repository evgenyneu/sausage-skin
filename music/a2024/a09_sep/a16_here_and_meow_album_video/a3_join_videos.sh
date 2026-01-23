#!/bin/bash
echo "Combine videos into one..."

# Concatenate All Videos into One
# Combine all the individual track and pause videos into a single video file.
ffmpeg -f concat -safe 0 -i concat_list.txt -c copy final_output.mp4


