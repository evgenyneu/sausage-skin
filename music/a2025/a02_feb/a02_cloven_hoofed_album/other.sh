# Convert MOV files to MP4 with matching video and audio codecs
ffmpeg -i output_3.mov -c:v libx264 -preset medium -crf 18 -c:a aac -b:a 320k -pix_fmt yuv420p output_3_converted.mp4

# Convert MOV to MP4 with correct 25fps frame rate
ffmpeg -i output_6.mov -c:v libx264 -preset medium -crf 18 \
    -c:a aac -b:a 320k -pix_fmt yuv420p \
    -r 25 -vsync cfr \
    output_6_converted.mp4

echo "Creating input file list with correct order..."
# Use the existing concat_list.txt which has the correct order
sed 's/output_3\.mov/output_3_converted.mp4/g; s/output_6\.mov/output_6_converted.mp4/g' concat_list.txt > inputs.txt
