import numpy as np
import matplotlib.pyplot as plt
import librosa
# from scipy import signal

wav,sr = librosa.load('noiseless.wav',mono=True)
print(wav.shape,sr)
# b, a = signal.butter(3, 0.05)
# zi = signal.lfilter_zi(b, a)
# z, _ = signal.lfilter(b, a, wav, zi=zi*wav[0])
# y = signal.filtfilt(b, a, wav)
plt.plot(wav)
# plt.plot(y)
plt.show()