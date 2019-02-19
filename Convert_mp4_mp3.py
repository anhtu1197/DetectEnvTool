import moviepy.editor as mp




def mp4_to_mp3(mp4path, dst_folder):
    clip = mp.VideoFileClip(mp4path)
    clip.audio.write_audiofile(dst_folder)
