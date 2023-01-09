from ctypes import *

winmm= windll.winmm
print('waveInGetNumDevs=', winmm.waveInGetNumDevs())