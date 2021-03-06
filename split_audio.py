import sox
import pydub
import os

def split_in_chunk(audio_filePath='', output_folder='', chunk= 10):
    filename = audio_filePath.split("/")[-1]

    output_folder = output_folder+'/output/'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    audio = pydub.AudioSegment.from_wav(audio_filePath)
    lenInSec = ( len(audio)/(chunk*1000)).__round__() #split each path by chunk second
    print( str(lenInSec))
    start = 0
    for i in range(0, lenInSec):
        audioPart = audio[start * 1000: (start + chunk) * 1000]
        audioPart.export(output_folder + '' + filename + str(i) + '.wav',
                         format="wav")  # Exports to a wav file in the current path.
        start += chunk



