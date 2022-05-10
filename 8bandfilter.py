'''import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

def plot_response(fs, w, h, title):
    "Utility function to plot response functions"
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(0.5*fs*w/np.pi, 20*np.log10(np.abs(h)))
    ax.set_ylim(-40, 5)
    ax.set_xlim(0, 0.5*fs)
    ax.grid(True)
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Gain (dB)')
    ax.set_title(title)

fs = 64000.0       # Sample rate, Hz
cutoff = 8000.0    # Desired cutoff frequency, Hz
trans_width = 100  # Width of transition from pass band to stop band, Hz
numtaps = 400      # Size of the FIR filter.
taps = signal.remez(numtaps, [0, cutoff, cutoff + trans_width, 0.5*fs], [1, 0], Hz=fs)
w, h = signal.freqz(taps, [1], worN=2000)
plot_response(fs, w, h, "Low-pass Filter")

plt.show() '''
import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt

N=8
b=signal.remez(8*N, [0,500,1000,2000,2500,16000], [0,1,0], [100,1,100],Hz=32000, type='bandpass')
#check the design:
plt.figure(figsize=(10,8))
plt.plot(b)
plt.title('Filter Impulse Response: Bandpass k=1, N=8')
plt.xlabel('Time in Samples')
plt.grid()

w,H=signal.freqz(b)
plt.figure(figsize=(10,8))
plt.plot(w,20*np.log10(abs(H)+1e-6))
plt.title('Filter Magnitude Frequency Response: Bandpass K=1, N=16')
plt.xlabel('Normalized Frequency')
plt.ylabel('dB')
plt.grid()
plt.show()
