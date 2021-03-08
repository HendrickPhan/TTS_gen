from pydub import AudioSegment
from pydub.silence import split_on_silence

files = [
    "DacNhanTam03.mp3" , 
    "DacNhanTam04.mp3", 
    "DacNhanTam05-1.mp3", 
    "DacNhanTam05-2.mp3", 
    "DacNhanTam06.mp3", 
    "DacNhanTam07.mp3",
    "DacNhanTam09.mp3",
    "DacNhanTam10.mp3",
] # change this to your files

for idx, file in enumerate(files):
    print("splitting " + file)
    sound_file = AudioSegment.from_mp3(file)
    dBFS = sound_file.dBFS
    audio_chunks = split_on_silence(sound_file, 
        # must be silent for at least half a second
        min_silence_len=300,

        # consider it silent if quieter than -16 dBFS
        silence_thresh= dBFS-16
    )
    for i, chunk in enumerate(audio_chunks):
        out_file = "./split/{0}_{1}.wav".format(idx, i)
        print("exporting", out_file)
        chunk.export(out_file, format="wav")