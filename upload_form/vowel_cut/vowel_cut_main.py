#!/usr/bin/python
# -*- Coding: utf-8 -*-

import wave
import numpy as np
import scipy.signal
import sys
import os

from upload_form.vowel_cut import wrapper_of_segmentation
from upload_form.vowel_cut import wave_Rel
from upload_form.vowel_cut import create_wav

UPLOADE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/input_file/'
DOWNLOADE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/wav_output/'
CUR_DIR=os.path.dirname(os.path.abspath(__file__))


def main(vowel):

    """音素ラベリング開始"""

    common = wrapper_of_segmentation.wrap_segment()

    if common == "No_number_of_files":
        return "No_number_of_files"
    if common == "No_extention":
        return "No_extention"
    if common == "No_match_filename":
        return "No_match_filename"
    if common == "No_Fs_check":
        return "No_Fs_check"

    #音声読み込み
    signal, fs = wave_Rel.waveread(UPLOADE_DIR+common+".wav")
    time = np.arange(0.0, len(signal)/fs, 1/fs)

    # julius_outputの labファイル読み込み
    f = open(CUR_DIR+'/julius_output/'+common+'.lab')
    lab_data = f.read().rstrip()  # ファイル終端まで全て読んだデータを返す
    f.close()

    # labファイルもユーザに出力
    file = open(DOWNLOADE_DIR+common + '-all.txt', 'w')  #書き込みモードでオープン
    file.write(lab_data)

    phonemes_times = lab_data.split('\n') # 改行で区切る(改行文字そのものは戻り値のデータには含まれない)
    for idx, phoneme_time in enumerate(phonemes_times):
        phonemes_times[idx] = phoneme_time.split(' ')

    for idx,phoneme_time in enumerate(phonemes_times):

        # 母音の前の子音を取得
        if idx == 0:
            consonant = "non"
        else:
            consonant = phonemes_times[idx-1][2]

        # 母音「あ」のとき
        if vowel == "a" and phoneme_time[2] == "a":
            # 対象の波形を切り出し
            cut_wav = signal[int(float(phoneme_time[0])*fs):int(float(phoneme_time[1])*fs)+1]
            # wavファイルに変換し保存
            filename = common + "_" + consonant + "_a_" + phoneme_time[0]
            create_wav.create_wavefile(filename,cut_wav)

        # 母音「い」のとき
        if vowel == "i" and phoneme_time[2] == "i":
            # 対象の波形を切り出し
            cut_wav = signal[int(float(phoneme_time[0])*fs):int(float(phoneme_time[1])*fs)+1]
            # wavファイルに変換し保存
            filename = common + "_" + consonant + "_i_" + phoneme_time[0]
            create_wav.create_wavefile(filename,cut_wav)

        # 母音「う」のとき
        if vowel == "u" and phoneme_time[2] == "u":
            # 対象の波形を切り出し
            cut_wav = signal[int(float(phoneme_time[0])*fs):int(float(phoneme_time[1])*fs)+1]
            # wavファイルに変換し保存
            filename = common + "_" + consonant + "_u_" + phoneme_time[0]
            create_wav.create_wavefile(filename,cut_wav)

        # 母音「え」のとき
        if vowel == "e" and phoneme_time[2] == "e":
            # 対象の波形を切り出し
            cut_wav = signal[int(float(phoneme_time[0])*fs):int(float(phoneme_time[1])*fs)+1]
            # wavファイルに変換し保存
            filename = common + "_" + consonant + "_e_" + phoneme_time[0]
            create_wav.create_wavefile(filename,cut_wav)

        # 母音「お」のとき
        if vowel == "o" and phoneme_time[2] == "o":
            # 対象の波形を切り出し
            cut_wav = signal[int(float(phoneme_time[0])*fs):int(float(phoneme_time[1])*fs)+1]
            # wavファイルに変換し保存
            filename = common + "_" + consonant + "_o_" + phoneme_time[0]
            create_wav.create_wavefile(filename,cut_wav)

    return common


if __name__ == '__main__':
    vowel = sys.argv[1]
    main(vowel)
