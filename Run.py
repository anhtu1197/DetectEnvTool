url = "" #url of youtube
home = "" #home folder
label = "" #label of the youtube source
from DataCollect import  get_data
from DataCollect import  merge_data
from DetectEnviroment import generate_all_spec
from DetectEnviroment import predict


# get_data("https://youtu.be/eSLe4HuKuK0", "/home/tupa4/Desktop/sample/testcollect/collect/", "phim1")
# get_data("https://youtu.be/RYKLUccJagQ", "/home/tupa4/Desktop/sample/testcollect/collect/", "phim2")
get_data("https://youtu.be/gHXKitKAT1E", "/home/tupa4/Desktop/sample/testcollect/collect/", "Beach")



merge_data("/home/tupa4/Desktop/sample/testcollect/collect/", "/home/tupa4/Desktop/sample/testcollect/home/")
#from now working in home dir

generate_all_spec("/home/tupa4/Desktop/sample/testcollect/home/audio/")

predict("/home/tupa4/Desktop/sample/testcollect/home/audio/", "/home/tupa4/Desktop/sample/testcollect/home/result/" )