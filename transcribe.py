# Note: you need to be using OpenAI Python v0.27.0 for the code below to work import openai
import openai
import os
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

# set input and output directories
input_dir = "./segment"
output_dir = "./result"

# get list of mp3 files in input directory
mp3_files = [f for f in os.listdir(input_dir) if f.endswith(".mp3")]
finished = [os.path.splitext(f)[0] for f in os.listdir(output_dir)]

# loop over mp3 files
for mp3_file in mp3_files:
    # read mp3 file
    print(mp3_file)
    if os.path.splitext(mp3_file)[0] in finished:
        print(mp3_file + " finished")
        continue
    audio_file= open(os.path.join(input_dir, mp3_file), "rb")

    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    mp3_file_out = os.path.splitext(mp3_file)[0]
    out_file_name = f"{mp3_file_out}.json"
 
    with open(os.path.join(output_dir, out_file_name), "w") as outfile:
        # Write the JSON object to the file
        json.dump(transcript, outfile)
    
        print(out_file_name + " finished") 
