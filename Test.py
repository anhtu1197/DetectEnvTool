
"""
ko lấy đoạn chuyển nữa à
padding dùng SoX:
sox input.wav output.wav pad xxx yyy
xxx: số giây silence muốn add vào bên trái
yyy: số giây silence muốn add vào bên phải
xxx, yyy có thể là số thực được
"""

from convert_audio import convert_rate

# def convertToWav(path):
#     print("Hello")
#
#
# import sox
import pydub
sound1 = pydub.AudioSegment.from_mp3("/home/tupa4/Desktop/sample/sample3/hongkong.mp3")
sound2 = pydub.AudioSegment.from_wav("/home/tupa4/Desktop/sample/sample3/hongkong.wav")#chia ra thanh nhieu doan 1s

print(len(sound1))
print(len(sound2))
#
# s = 0
#
# lenInSec = (len(sound)/10000).__round__()
#
# path = '/home/tupa4/Desktop/sample/sample1/export/'
#
# for i in range (0, lenInSec):
#     audioPart = sound[s*1000: (s + 10)*1000]
#     audioPart.export( path + 'hongkong' + str(i) + '.wav', format="wav") #Exports to a wav file in the current path.
#     s += 10
#
#



# sound.export("/home/tupa4/Desktop/sample/hongkong.wav", format="wav")
#
# convert_rate("/home/tupa4/Desktop/sample/sample1","/home/tupa4/Desktop/sample/sample2")

# tmf = sox.Transformer()
# tmf.downsample(3)
# tmf.build("/home/tupa4/Desktop/sample/sample1/hongkong.mp3", "/home/tupa4/Desktop/sample/test.wav")

from split_audio import  split_in_chunk

split_in_chunk(audio_filePath="/home/tupa4/Desktop/sample/sample3/hongkong.wav", output_folder="/home/tupa4/Desktop/sample/sample3/output/")
