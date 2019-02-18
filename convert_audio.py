import os
import subprocess
#441001
def convert_rate(src_folder='', dst_folder='', RATE='16000'):
    if not os.path.isdir(src_folder):
        print("Source folder doesn't exist")
        return
    if not os.path.isdir(dst_folder): 
        os.makedirs(dst_folder)

    fns = [fn for fn in os.listdir(src_folder) if 
                any(map(fn.endswith, ['.mp3', '.wav', '.amr']))]

    for i, fn in enumerate(fns): 
        old_fn = os.path.join(src_folder, fn) 
        new_fn = os.path.join(dst_folder, fn.split('.')[0] + '.wav')

        if os.path.isfile(new_fn): 
            continue
        # convert all file to wav, mono, sample rate 16000
        subprocess.call(['ffmpeg', '-loglevel', 'panic', '-i',  old_fn, 
                '-acodec', 'pcm_s16le', '-ac', '1', '-ar', RATE, new_fn])
        if (i+1)%10 == 0:
            print('{}/{}: {}'.format(i+1, len(fns), new_fn))


if __name__ == '__main__':
    convert_rate(src_folder='', dst_folder='', RATE='16000')

