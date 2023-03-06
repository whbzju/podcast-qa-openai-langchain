import os
from pydub import AudioSegment

# set input and output directories
input_dir = "./source"
output_dir = "./segment"

print(input_dir, output_dir)

# get list of mp3 files in input directory
mp3_files = [f for f in os.listdir(input_dir) if f.endswith(".mp3")]

print(mp3_files)

# loop over mp3 files
for mp3_file in mp3_files:
    # read mp3 file
    audio = AudioSegment.from_file(os.path.join(input_dir, mp3_file), format="mp3")

    # calculate number of 20 minute segments
    num_segments = (len(audio) // (20 * 60 * 1000)) + 1

    # loop over segments and save to output directory
    for i in range(num_segments):
        # calculate start and end time in milliseconds
        start_time = i * 20 * 60 * 1000
        end_time = min((i + 1) * 20 * 60 * 1000, len(audio))

        # get segment audio and set filename
        segment_audio = audio[start_time:end_time]
        segment_filename = f"{os.path.splitext(mp3_file)[0]}_{i+1}.mp3"

        # save segment audio to output directory
        segment_audio.export(os.path.join(output_dir, segment_filename), format="mp3")

print("done")
