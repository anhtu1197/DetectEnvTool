import sox
import pydub


def split_in_chunk(audio_filePath='', output_folder='', chunk= 10):
    audio = pydub.AudioSegment.from_wav(audio_filePath)
    lenInSec = ( len(audio)/(chunk*1000)).__round__() #split each path by chunk second
    print( str(lenInSec))
    start = 0
    for i in range(0, lenInSec):
        audioPart = audio[start * 1000: (start + chunk) * 1000]
        audioPart.export(output_folder + '' + str(i) + '.wav',
                         format="wav")  # Exports to a wav file in the current path.
        start += chunk



