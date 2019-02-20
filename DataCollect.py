from youtubeDownloader import downloadYouTube
from Convert_mp4_mp3 import  mp4_to_mp3
import  os
from  convert_audio import convert_rate
from split_audio import  split_in_chunk
from metadata_maker import make_meta
import  shutil
#https://youtu.be/eSLe4HuKuK0


def merge_data(src, dst_folder):
    #move audio
    for filename in (os.listdir(src + "/output")):
        shutil.move(src + "/output/" + filename, dst_folder + 'audio/')
    #merge meta data
    with open(dst_folder + 'meta.txt', "a") as outfile:
        with open(src + 'outputmeta.txt') as infile:
            outfile.write(infile.read())

def get_data(url, dst_folder, label):
    #download from youtube
    downloadYouTube(videourl=url, path=dst_folder)
    #Convert mp4 to mp3
        #need to find the mp4 filenames
    filenames = []
    for filename in os.listdir(dst_folder):
        if filename.endswith(".mp4"):
            filenames.append(filename)
        #now convert to mp3
    for filename in filenames:
        mp4_to_mp3(dst_folder + filename, dst_folder + filename.replace(" ", "") + ".mp3")
    #now convert to wav
    convert_rate(dst_folder , dst_folder + 'wav/', RATE= "44100")
    #split in to chunk with metadata
    for filename in (os.listdir(dst_folder + 'wav/')):
        if filename.endswith(".wav"):
            print(filename)
            split_in_chunk(audio_filePath= dst_folder + 'wav/' + filename, output_folder=dst_folder)
    #make meta data
    make_meta(dst_folder + '/output', label)
    #get source & metadata to merge in to largefolder





#get_data("https://youtu.be/eSLe4HuKuK0", "/home/tupa4/Desktop/sample/tu/", "phim")
#merge_data('/home/tupa4/Desktop/sample/tu/', '/home/tupa4/Desktop/sample/datatu/')