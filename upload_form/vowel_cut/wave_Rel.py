import wave
import numpy as np
import scipy.signal

#音声ファイル読み込み(適宜調整)
def waveread(filename):
    wf = wave.open(filename, "rb")
    fs = wf.getframerate() #16000Hz
    #getnframes > 全サンプル, readframes > 指定した長さのフレーム
    x = wf.readframes(wf.getnframes())
    #frombuffer > バイナリ表記をintに変換
    x = np.frombuffer(x, dtype="int16") #/ 32768.0 #(-1, 1)に正規化
    wf.close()
    return x, float(fs)

#音声の正規化
def normalize(signal):
    sMax = signal.max()
    sMin = np.abs(signal.min())
    if sMax < sMin:
        sMax = sMin
    signal = signal / sMax
    return signal
