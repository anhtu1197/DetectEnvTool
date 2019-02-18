import os

def make_meta(src_folder = '', label = 'empty'):
    #go through all filename in an directory
    #label the
    filenames = os.listdir(src_folder)
    for filename in filenames:
        with open(src_folder + "meta.txt", "a") as f:
            f.write(filename + "\t" + label + "\n")

