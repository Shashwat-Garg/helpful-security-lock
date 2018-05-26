'''
#!/usr/bin/env python

from __future__ import print_function

import sys
import time
import getopt
import alsaaudio

def usage():
    print('usage: recordtest.py [-d <device>] <file>', file=sys.stderr)
    sys.exit(2)

if __name__ == '__main__':

    device = 'default'

    opts, args = getopt.getopt(sys.argv[1:], 'd:')
    for o, a in opts:
        if o == '-d':
            device = a

    if not args:
        usage()

    f = open(args[0], 'wb')

    # Open the device in nonblocking capture mode. The last argument could
    # just as well have been zero for blocking mode. Then we could have
    # left out the sleep call in the bottom of the loop
    inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK, device=device)

    # Set attributes: Mono, 44100 Hz, 16 bit little endian samples
    inp.setchannels(1)
    inp.setrate(44100)
    inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)

    # The period size controls the internal number of frames per period.
    # The significance of this parameter is documented in the ALSA api.
    # For our purposes, it is suficcient to know that reads from the device
    # will return this many frames. Each frame being 2 bytes long.
    # This means that the reads below will return either 320 bytes of data
    # or 0 bytes of data. The latter is possible because we are in nonblocking
    # mode.
    inp.setperiodsize(160)
    
    loops = 1000000
    while loops > 0:
        loops -= 1
        # Read data from device
        l, data = inp.read()
      
        if l:
            f.write(data)
            time.sleep(.001)
'''

'''
import pyaudio
import wave

CHUNK = 512
FORMAT = pyaudio.paInt16 #paInt8
CHANNELS = 1
RATE = 44100 #sample rate
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "pyaudio-output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK) #buffer

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK,exception_on_overflow=False)
    frames.append(data) # 2 bytes(16 bits) per channel

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
'''
'''
import pyaudio
po = pyaudio.PyAudio()
for index in range(po.get_device_count()): 
    desc = po.get_device_info_by_index(index)
    if desc["name"] == "record":
        print "DEVICE: %s  INDEX:  %s  RATE:  %s " %  (desc["name"], index,  int(desc["defaultSampleRate"]))
'''

import sys, os
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *
import pyaudio

modeldir = "../../../model"
datadir = "../../../test/data"

# Create a decoder with certain model
config = Decoder.default_config()
config.set_string('-hmm', os.path.join(modeldir, 'en-us/en-us'))
config.set_string('-dict', os.path.join(modeldir, 'en-us/cmudict-en-us.dict'))
config.set_string('-keyphrase', 'forward')
config.set_float('-kws_threshold', 1e+20)


p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
stream.start_stream()

# Process audio chunk by chunk. On keyword detected perform action and restart search
decoder = Decoder(config)
decoder.start_utt()
while True:
    buf = stream.read(1024)
    if buf:
         decoder.process_raw(buf, False, False)
    else:
         break
    if decoder.hyp() != None:
        print ([(seg.word, seg.prob, seg.start_frame, seg.end_frame) for seg in decoder.seg()])
        print ("Detected keyword, restarting search")
        decoder.end_utt()
        decoder.start_utt()
