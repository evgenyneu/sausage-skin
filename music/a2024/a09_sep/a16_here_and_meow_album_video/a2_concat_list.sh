#!/bin/bash
echo "Create concatenation list..."

# Create a Concatenation List:
# Prepare a text file that lists all the videos in the order
# they should be concatenated.
for i in {1..11}; do
    echo "file 'pause_${i}.mp4'" >> concat_list.txt
    echo "file 'output_${i}.mp4'" >> concat_list.txt
    echo "file 'pause_${i}.mp4'" >> concat_list.txt
done

# echo "file 'output_11.mp4'" >> concat_list.txt
# echo "file 'pause_11.mp4'" >> concat_list.txt


