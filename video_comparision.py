import os

def create_codec_comparison(codec1, codec2, resolution='720p'):
    input_file1 = '/mnt/d/Download/s3_scav/BBB60.mp4-VP8.webm'
    input_file2 = '/mnt/d/Download/s3_scav/BBB60.mp4-VP9.webm'
    output_file = f'comparison_{codec1}_vs_{codec2}_{resolution}.mp4'

    # Combine videos side by side
    os.system(f'ffmpeg -i {input_file1} -i {input_file2} -filter_complex hstack=inputs=2 {output_file}')

    print(f'Comparison video ({resolution}): {output_file}')

if __name__ == "__main__":
    # Choose the codecs you want to compare
    codec1 = 'VP8'
    codec2 = 'VP9'

    # Choose the resolution
    resolution = '720p'

    # Create the video comparison
    create_codec_comparison(codec1, codec2, resolution)
'''
VP9 generally provides better compression efficency that VP8. This means that,at the
same bitrate, VP9 can deliver higher quality. VP8 is less efficient compared to VP9.
