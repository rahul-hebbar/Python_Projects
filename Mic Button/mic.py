import sounddevice as sd
import numpy as np
import keyboard
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_data,y_data = [],[]
fig = plt.figure()
line, = plt.plot_date(x_data,y_data,'-')

def update(frame):
    x_data.append(np.arange(frame.shape[0]))
    y_data.append(frame)
    line.set_data(x_data,y_data)
    fig.gca().relim()
    fig.gca().autoscale_view()
    return line

def callback(indata,frames,time,status):
    if status:
        print(status)
    print(f"indata shape: {indata.shape}")
    animation = FuncAnimation(fig,update(indata.reshape(-1,)),interval=40)

with sd.InputStream(channels=1,samplerate=16000,callback=callback):
    plt.show()
    # keyboard.wait('q')
    # sd.sleep(137)

