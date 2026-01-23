ffmpeg -i criticism_of_our_socio_economic_system.mp4 -ss 20.130 -c copy criticism_of_our_socio_economic_system_cropped.mp4

ffmpeg -i criticism_of_our_socio_economic_system.mp4 -force_key_frames 20.130 -c:v libx264 -preset fast -crf 23 -c:a copy criticism_of_our_socio_economic_system_cropped.mp4

ffmpeg -ss 20.130 -i criticism_of_our_socio_economic_system.mp4 -force_key_frames 0 -c:v libx264 -preset fast -crf 23 -c:a copy criticism_of_our_socio_economic_system_cropped.mp4

