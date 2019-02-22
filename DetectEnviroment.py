import numpy as np
import os
import  librosa
import  keras
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import librosa
import numpy as np
os.environ['KERAS_BACKEND'] = 'theano'
import keras
keras.backend.set_image_data_format('channels_first')
from keras import backend as K
from keras.models import Model
from keras.activations import softmax
from keras.layers import Input, concatenate
from keras.layers.convolutional import Conv2D
from keras.layers.pooling import GlobalAveragePooling2D, GlobalMaxPooling2D
from keras.layers.advanced_activations import LeakyReLU
from keras.layers.core import Activation, Dense, Dropout, Flatten, Reshape, Lambda, RepeatVector
from keras.callbacks import LearningRateScheduler, Callback, ModelCheckpoint
from keras.layers.normalization import BatchNormalization
from keras.models import load_model
import keras.models


def generate_spec(recording, bands ='stft'):
    spec_file = str(recording) + '.spec' + str(bands) + '.npy'

    if os.path.exists(spec_file):
        return

    audio, _ = librosa.core.load(recording, sr=44100, dtype= np.float16, duration=10.0)

    if bands == 'stft':
        spec = np.abs(librosa.stft(audio, n_fft=2205, hop_length=882))
    else:
        spec = librosa.feature.melspectrogram(audio, sr=44100, n_fft=2205, hop_length=882,
                                              n_mels=bands, fmax=22050, power=2)
    spec = librosa.power_to_db(spec)

    np.save(spec_file, spec.astype('float16'), allow_pickle=False)


def load_spec(recording, bands = 'stft'):
    return np.load(recording).astype('float32')




def generate_all_spec(src):
    for filename in os.listdir(src):
        if filename.endswith(".wav"):
             generate_spec(src + filename, bands=200)





def predict(src, result_dst, label):
    labels = ['beach', 'bus', 'cafe/restaurant', 'car', 'city_center', 'forest_path',
              'grocery_store', 'home', 'library', 'metro_station', 'office', 'park',
              'residential_area', 'train', 'tram']


    BANDS = 200 #need to edit
    inputs = Input(shape=(1, BANDS, 500))

    x = Conv2D(100, kernel_size=(BANDS, 50), kernel_initializer='he_uniform')(inputs)
    x = BatchNormalization(axis=1)(x)
    x = LeakyReLU()(x)
    x = Dropout(0.25)(x)

    x = Conv2D(100, kernel_size=(1, 1), kernel_initializer='he_uniform')(x)
    x = BatchNormalization(axis=1)(x)
    x = LeakyReLU()(x)
    x = Dropout(0.25)(x)

    x = Conv2D(15, kernel_size=(1, 1), kernel_initializer='he_uniform')(x)
    x = Lambda(softmax, arguments={'axis': 1}, name='softmax')(x)

    x = GlobalAveragePooling2D()(x)

    model = Model(inputs=inputs, outputs=x)
    model.compile(loss='categorical_crossentropy', optimizer=keras.optimizers.Adam(lr=0.001),
                  metrics=['accuracy'])
    #
    model.load_weights("/home/tupa4/Desktop/DCASE/2017/paper-2017-DCASE/Code/results/run_200_all_all.h5")




    # model.predict_generator(spec, steps=1)

    # predict = model.predict(spec)
    # print(predict)
    # predict = np.argmax(predict, axi s=1)
    # predict = int(predict)
    # print(predict)



    #Go and predict all the spec

    files = []
    predictions = []


    for filename in os.listdir(src):
        if filename.endswith(".npy"):
            print(filename)
            spec  = load_spec(src + filename)
            print(spec.shape)
            try:
                spec = np.array([spec.reshape(1, 200, 500)])
                predict = model.predict(spec)
                predict = np.argmax(predict, axis=1)
                predict = int(predict)
                predict = labels[predict]
            except:
                print("ERROR!")
                predict = "ERROR!"
            files.append(filename)
            print("File name " + filename.split(".")[0])
            predictions.append(predict)
    print("Hello")
    print(predictions)
    print(files)
    #correction
    count = 0
    for result in predictions:
        if (result == label):
            count += 1
    results = pd.DataFrame({'file': files, 'scene': predictions},
                           columns=['file', 'scene'])
    print(results)

    print("Correction = " + str(count/len(predictions)))






    if  (not os.path.exists(result_dst + "result")):
        os.mkdir(result_dst + "result")
    results.to_csv(result_dst+ "kqua" +  '.csv', sep='\t', index=False, header=True)

    #print("Hi")
    #using the
    #print("Result " + labels[predict])



#path = "/home/tupa4/Desktop/sample/tu/output/"

#generate_all_spec(path)

#predict("/home/tupa4/Desktop/sample/tu/output/", "/home/tupa4/Desktop/sample/tu/test/" )