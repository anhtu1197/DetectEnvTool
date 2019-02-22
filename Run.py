url = input("Enter URL!\n")
download_folder = ""
home_folder = "" #home folder
label = input("Enter label!\n")
from DataCollect import  get_data
from DataCollect import  merge_data
from DetectEnviroment import generate_all_spec
from DetectEnviroment import predict


get_data(url, "/home/tupa4/Desktop/sample/testcollect/collect/", label)



merge_data("/home/tupa4/Desktop/sample/testcollect/collect/", "/home/tupa4/Desktop/sample/testcollect/home/")
#from now working in home dir
generate_all_spec("/home/tupa4/Desktop/sample/testcollect/home/audio/")
predict("/home/tupa4/Desktop/sample/testcollect/home/audio/", "/home/tupa4/Desktop/sample/testcollect/home/result/" , label)

# labels = ['beach', 'bus', 'cafe/restaurant', 'car', 'city_center', 'forest_path',
#           'grocery_store', 'home', 'library', 'metro_station', 'office', 'park',
#           'residential_area', 'train', 'tram']