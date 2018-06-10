import numpy, wave, array
import os

DOWNLOADE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/wav_output/'

def create_wavefile(filename,data):
    filename = DOWNLOADE_DIR + filename + ".wav"

    # save wav file
    buf = data
    w = wave.Wave_write(filename)
    w.setparams((
        1,                        # channel
        2,                        # byte width
        16000,                    # sampling rate
        len(buf),                 # number of frames
        "NONE", "not compressed"  # no compression
    ))
    w.writeframes(array.array('h', buf).tostring())
    w.close()

    return
