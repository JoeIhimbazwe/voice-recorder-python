import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv 


freq = 44100
duration = 25

recording = sd.rec(int(duration * freq), samplerate=freq, channels=1)


sd.wait()

write("recording-gfg.wav", freq, recording)

wv.write("recording-gfg-1.wav", recording, freq, samplewidth=2)