
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
# import pydub
# sound1 = pydub.AudioSegment.from_mp3("/home/tupa4/Desktop/sample/sample3/hongkong.mp3")
# sound2 = pydub.AudioSegment.from_wav("/home/tupa4/Desktop/sample/sample3/hongkong.wav")#chia ra thanh nhieu doan 1s
#
# print(len(sound1))
# print(len(sound2))
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

# from split_audio import  split_in_chunk
#
# split_in_chunk(audio_filePath="/home/tupa4/Desktop/sample/sample3/hongkong.wav", output_folder="/home/tupa4/Desktop/sample/sample3/")
# import os
# t = os.listdir("/home/tupa4/Desktop/DCASE/2017/datasets/TUT-acoustic-scenes-2017-evaluation/evaluation_setup")
# print(t)

# with open("foo.txt", "a") as f:
#     f.write("Haha\n")
# import os
#
# filenames = os.listdir("/home/tupa4/Desktop/sample/sample3/output/")
# # with open("foo.txt", "a") as f:
# #     f.write("Haha\n")
# label = 'music'
# for filename in filenames:
#     print(filename)
#     with open("foo.txt", "a") as f:
#         f.write(filename +"\t" + label + "\n")

#
# from metadata_maker import make_meta
#
#
# make_meta("/home/tupa4/Desktop/sample/sample3/output/", "music")
import os
#
# from pytube import YouTube
# path = '/home/tupa4/Desktop/sample/tu'
# videourl = 'https://youtu.be/eSLe4HuKuK0'
# yt = YouTube(videourl)
# yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
# if not os.path.exists(path):
#     os.makedirs(path)
#     yt.download(path)
#
#

import subprocess
# filename = "/home/tupa4/Desktop/sample/tu/test.mp4"
# import moviepy.editor as mp
# clip = mp.VideoFileClip(filename)
# clip.audio.write_audiofile("/home/tupa4/Desktop/sample/tu/theaudio.mp3")


# path = 'tu/home/do/today'.split("/")[-1]
# print(path)
# to = []
# for t in path.split("/"):
#     print(t)
#
# name = "hu lu lu"
# print(name.replace(" ", ""))

#
# name = "Frozen2OfficialTeaserTrailer.wav5.wav.specstft.npy".split(".")[0]
# print(name)
# import pandas as pd
#
# df2 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['a', 'b', 'c'])
#

# print(df2)
#
# recording = "/home/tupa4/Desktop/sample/tu/output/Frozen2OfficialTeaserTrailer.wav0.wav.specstft.npy"
#
# spec  = np.load(recording).astype('float32')
#
# print(spec.shape)
import numpy as np
# import pandas as pd
# file = ['Frozen2OfficialTeaserTrailer.wav10.wav.spec200.npy', 'Frozen2OfficialTeaserTrailer.wav3.wav.spec200.npy', 'Frozen2OfficialTeaserTrailer.wav2.wav.spec200.npy', 'Frozen2OfficialTeaserTrailer.wav7.wav.spec200.npy', 'Frozen2OfficialTeaserTrailer.wav5.wav.spec200.npy', 'Frozen2OfficialTeaserTrailer.wav9.wav.spec200.npy', 'Frozen2OfficialTeaserTrailer.wav8.wav.spec200.npy', 'Frozen2OfficialTeaserTrailer.wav4.wav.spec200.npy', 'Frozen2OfficialTeaserTrailer.wav6.wav.spec200.npy', 'Frozen2OfficialTeaserTrailer.wav0.wav.spec200.npy', 'Frozen2OfficialTeaserTrailer.wav1.wav.spec200.npy']
#
# predict = ['park', 'car', 'park', 'park', 'park', 'park', 'residential_area', 'park', 'park', 'car', 'residential_area']
#
# results = pd.DataFrame({'file': file, 'scene': predict},
#                        columns=['file', 'scene'])
#
# print(results)

#file = "Cul-de-SacOfficialTrailer1(2016)-ShortFilm.wav8.wav.spec200.npy"

#
# path = "/home/tupa4/Desktop/sample/sample1/"
# import shutil
# shutil.rmtree(path)

#
# name = input("What is your name? ")
# print(name)

# import pandas as pd
#
# df = pd.read_csv("/home/tupa4/Desktop/sample/testcollect/home/result/" + "kqua.csv", parse_dates=True)
#
# print(df.head())

dst = "/home/tupa4/Desktop/sample/testcollect/home/"
if(os.path.exists(dst + "audio")):
    print("exist")
os.mkdir(dst + "/audio/")