#!/usr/bin/python
# -*- Coding: utf-8 -*-

import glob

import subprocess
from upload_form.vowel_cut import conf
import os

UPLOADE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/input_file/'
DOWNLOADE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/wav_output/'
CUR_DIR=os.path.dirname(os.path.abspath(__file__))

def wrap_segment():
    """
    音素ラベリングセグメンテーションが実装された「segmentation-kit」を使いやすくしたもの
    input_fileディレクトリの中にファイル名が同じ2つのファイル「.txt」「.wav」を準備すること
    出力先はjulius_outputに格納される
    返り値は共通するファイルネーム
    """

    """入力ファイル(数およびファイル名)の確認"""
    input_files = glob.glob(UPLOADE_DIR+"*")

    # ファイル数の確認
    if conf.number_of_files(input_files) == -1:
        return "No_number_of_files"
    # 拡張子の確認
    if conf.extention(input_files) == -1:
        return "No_extention"
    # ファイル名一致か否か
    common,err = conf.match_filename(input_files)
    if err == -1:
        return "No_match_filename"

    # wavファイルのサンプリングレートが適切か
    if conf.Fs_check(common) == -1:
        return "No_Fs_check"


    """主なwrapper部分"""
    subprocess.call( ["rm", "-r", CUR_DIR+"/segmentation-kit/wav"] )
    subprocess.call( ["cp", "-r", CUR_DIR+"/input_file",CUR_DIR+"/segmentation-kit/wav"] )

    #ディレクトリを移動して実行
    subprocess.call( ["perl", "segment_julius.pl"], cwd=CUR_DIR+'/segmentation-kit' )

    subprocess.call( ["rm", CUR_DIR+"/julius_output/*"] )
    subprocess.call( ["cp", CUR_DIR+"/segmentation-kit/wav/"+common+".log", CUR_DIR+"/julius_output/"] )
    subprocess.call( ["cp", CUR_DIR+"/segmentation-kit/wav/"+common+".lab", CUR_DIR+"/julius_output/"] )

    return common

if __name__ == '__main__':
    wrap_segment()
