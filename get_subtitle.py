import os
import time
from get_response import *

lines = list(open("subtitles.csv", 'r'))
processedFiles = list()
for line in lines:
    splits = line.split("|")
    processedFiles.append(splits[0])
print(processedFiles)
audio_path = os.path.abspath(os.getcwd()) + '/split/'
subtitle_file = open("subtitles.csv", "a")

audios = os.listdir(audio_path)
for index, audio_file in enumerate(audios):
    print("running file " + audio_path + audio_file)
    if audio_file in processedFiles:
        print("processed") 
    else:
        try:
            rs = call_zalo_api(audio_file)
            with open('subtitles.csv', 'a') as f:
                f.write("{0}|{1}\n".format(audio_file, rs))
        except:
            print("e")
            continue

subtitle_file.close()