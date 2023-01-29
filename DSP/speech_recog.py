import os
import librosa
import librosa.display 
import numpy as np
import python_speech_features as psf
import matplotlib.pyplot as plt

def gen_npy():
    path = ".\\wavs"
    # data = np.zeros((2000,22050,1))
    # label = np.zeros((2000,1))
    # fg = 0
    for j in os.listdir(path):
        class_path = os.path.join(path,j)
        for i in os.listdir(class_path):
            wa,sr = librosa.load(os.path.join(class_path,i),mono=True)
            mfcc = psf.mfcc(wa,nfft=512)
            librosa.display.specshow(mfcc.T)
            plt.show()
            print(f'{i} - {mfcc.shape}')
            break
            # data[fg] = wav
            # label[fg] = int(j)
            # fg += 1
    # print(data[0:10],label[0:10])
    # print(data.shape,label.shape)
    # np.save('data.npy',data)
    # np.save('label.npy',label)

gen_npy()
# data = np.load('data.npy')
# label = np.load('label.npy')

# print(data.shape)
# from sklearn.model_selection import train_test_split
# import tensorflow as tf

# x_train, x_test, y_train, y_test = train_test_split(data,label, test_size=0.33, random_state=42)
# x_train = tf.keras.utils.normalize(x_train)
# y_train = tf.keras.utils.normalize(y_train)
