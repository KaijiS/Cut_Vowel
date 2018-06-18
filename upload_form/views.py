from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.conf import settings
from django.http import HttpResponse
from upload_form.models import FileNameModel
import sys, os
UPLOADE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/vowel_cut/input_file/'
DOWNLOADE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/vowel_cut/wav_output/'

import glob
import subprocess

from io import BytesIO
import zipfile

from upload_form.vowel_cut import vowel_cut_main

def form(request):
    if request.method != 'POST':
        return render(request, 'upload_form/form.html')

    vowel = request.POST.get('vowel')

    # 前回のファイル削除
    file_list = glob.glob(UPLOADE_DIR+'*')
    for file_name in file_list:
        subprocess.call(["rm", file_name])

    file_list = glob.glob(DOWNLOADE_DIR+'*')
    for file_name in file_list:
        subprocess.call(["rm", file_name])

    # アップロードファイルの取得
    files = request.FILES.getlist("file[]")
    for file in files:
        path = os.path.join(UPLOADE_DIR, file.name)
        destination = open(path, 'wb')

        for chunk in file.chunks():
            destination.write(chunk)

        insert_data = FileNameModel(file_name = file.name)
        insert_data.save()

    # 母音抽出及び、ファイルチェック
    common = vowel_cut_main.main(vowel)

    flag = 0
    if common == "No_number_of_files":
        flag = 1
        comment = "拡張子が「.wav」と「.txt」の2種類のみにしてください"
    if common == "No_extention":
        flag = 1
        comment = "拡張子が違います\n拡張子が「.wav」と「.txt」の2種類のみにしてください"
    if common == "No_match_filename":
        flag = 1
        comment = "ファイル名を一致させてください"
    if common == "No_Fs_check":
        flag = 1
        comment = "サンプリング周波数を16000Hzにしてください"

    if flag != 0:
        content = {
            'comment':comment
        }
        return render(request, 'upload_form/form.html',content)

    content = {
        'vowel':vowel,
        'common':common
    }


    return render(request, 'upload_form/complete.html',content)



def download(request):
    vowel = request.POST.get('vowel')
    common = request.POST.get('common')


    memory_file = BytesIO()
    phoneme_zip = zipfile.ZipFile(memory_file, 'w')

    file_list = glob.glob(DOWNLOADE_DIR+'*')

    for file_part in file_list:
        file_name = file_part.replace(DOWNLOADE_DIR,"")
        phoneme_zip.writestr(file_name , open(file_part ,'rb').read())


    phoneme_zip.close()
    response = HttpResponse(memory_file.getvalue(), content_type="application/zip")
    response['Content-Disposition'] = 'attachment; filename={}_cut.zip'.format(common)
    return response
