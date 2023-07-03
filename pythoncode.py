import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment
from scipy import fft

classes = ['Sub-Bass','Bass','Lower midrange','Midrange','Higher midrange','Presence','Brilliance']

audio_file  = 'test_audio.mp3' #Audio file to be used

audio = AudioSegment.from_mp3(audio_file) #Reading Audio file

#Converting to Numpy Array
audio_data = np.array(audio.get_array_of_samples())

#Applying Fourier Transform to the audio signal. Since amplitude can be complex, we calculate the magnitude
amplitude = np.abs(fft.rfft(audio_data))
frequency = fft.rfftfreq(len(audio_data), 1/audio.frame_rate)


max_amplitude = max(amplitude)
cuttoff = max_amplitude/100

temp = [0,0,0,0,0,0,0]
#Checking which class(es) the audio belongs to
for j in range(len(frequency)):
    i = frequency[j]
    if(amplitude[j] > cuttoff):
        if( i < 60):
            temp[0] = 1
        elif ( i < 250):
            temp[1] = 1
        elif ( i < 500):
            temp[2] = 1
        elif ( i < 2000):
            temp[3] = 1
        elif ( i < 4000):
            temp[4] = 1
        elif ( i < 6000):
            temp[5] = 1
        elif ( i < 20000):
            temp[6] = 1
print('The audio belongs to the following classes:')
for i in range(7):
    if(temp[i]):
        print(classes[i])


plt.plot(frequency,amplitude)
plt.xlabel('Frequency')
plt.show()
