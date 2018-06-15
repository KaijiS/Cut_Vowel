#!/usr/bin/python
# -*- Coding: utf-8 -*-

import os

from upload_form.vowel_cut import wave_Rel

UPLOADE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/input_file/'

"""
入力ファイル(数およびファイル名)の確認
"""

def number_of_files(input_files):
    """ファイル数の確認"""
    """
    入力：ファイル名が要素となるリスト
    返り値：ファイル数2のとき:0, 2以外の時:-1
    """
    if len(input_files) != 2:
        print("拡張子が「.wav」と「.txt」である2種類のみデータにしてください")
        return -1
    return 0

def extention(input_files):
    """拡張子の確認"""
    """
    入力：ファイル名が要素となるリスト
    出力：指定された拡張子の時：0　それ以外の時：-1
    """
    txt_flag = 0
    wav_flag = 0
    flag = 0
    for idx,file_name in enumerate(input_files):
        if file_name.find('.txt') == -1 and file_name.find('.wav') == -1:
            flag = 1
            break
        elif idx == 0:
            if file_name.find('.txt') != -1:
                txt_flag = 1
            elif file_name.find('.wav') != -1:
                wav_flag = 1
        else:
            if txt_flag == 1 and file_name.find('.txt') != -1:
                flag = 1
                break
            elif wav_flag == 1 and file_name.find('.wav') != -1:
                flag = 1
                break

    if flag == 1:
        print("拡張子が違います")
        print("拡張子が「.wav」と「.txt」である2種類のみデータにしてください")
        return -1

    return 0

def match_filename(input_files):
    """ファイル名一致か否か"""
    """
    入力：ファイル名が要素となるリスト
    出力：ファイル名, ファイル名一致の時：0　不一致の時：-1
    """
    flag = 0
    for idx,file_name in enumerate(input_files):
        file_name = file_name.replace(UPLOADE_DIR,"")
        if idx == 0:
            if file_name.find('.txt') != -1:
                common = file_name.replace(".txt","")
            else:
                common = file_name.replace(".wav","")
        else:
            if file_name.find('.txt') != -1:
                if common != file_name.replace(".txt",""):
                    flag = 1
                    common = ".."
                    break
            else:
                if common != file_name.replace(".wav",""):
                    flag = 1
                    common = ".."
                    break

    if flag == 1:
        print("ファイル名を一致させてください")
        return common,-1

    return common,0

def Fs_check(common):
    filename = UPLOADE_DIR+common+".wav"
    wave,fs = wave_Rel.waveread(filename)

    if fs != 16000:
        print("サンプリング周波数が16000Hzであるwavデータにしてください")
        return -1
    return 0
