import numpy as np
import os
import  librosa
import  keras

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


def _load_spec(self, recording, bands = 'stft'):
    return np.load(recording + '.spec' + str(bands) + '.npy').astype('float32')




def generate_all_spec(src):
    for filename in os.listdir(src):
        if filename.endswith(".wav"):
             generate_spec(src + filename)
path = "/home/tupa4/Desktop/sample/tu/output/"

generate_all_spec(path)


def predict(src, result_dst):
    BANDS = 200
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
    # predict = np.argmax(predict, axis=1)
    # predict = int(predict)
    # print(predict)


    labels = ['beach', 'bus', 'cafe/restaurant', 'car', 'city_center', 'forest_path',
              'grocery_store', 'home', 'library', 'metro_station', 'office', 'park',
              'residential_area', 'train', 'tram']
    for filename in os.listdir(src):
        if filename.endswith(".npy"):
             generate_spec(src + filename)

    print("Result " + labels[predict])





