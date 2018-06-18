# Cut_Vowel

**音素自動セグメンテーションを用いた母音波形抽出webアプリ**

## 開発環境  
- OS: ubuntu 14.04LTS   
- 開発言語:
  - perl 5.18.2(Julius内)
  - python3 3.4.3
- 使用したツール:
  - Julius 4.2.2
  - pip3 10.0.1
- 必要なライブラリ:
  - numpy 1.13.3
  - scipy 0.13.3
  - Django 2.0.6(ウェブアプリケーションフレームワーク)

## 環境構築，サーバ起動方法およびwebアプリアクセス方法(Ubuntu14.04)  
1. 必要な言語およびライブラリのインストール  
`sudo apt install perl`  
`sudo apt install python3-pip`  
`sudo pip3 install numpy`  
`sudo pip3 install scipy`  
`sudo pip3 install django`  

2. Juliusのインストール
任意のディレクトリで  
`git clone https://github.com/julius-speech/julius`  
`cd julius`  
`./configure`  
`make`  
`sudo make install`  
/usr/local/bin/julius があることを確認 ・・・①

3. 本アプリをクローン  
webアプリ用ディレクトリで  
`git clone https://github.com/KaijiS/Cut_Vowel`  
 /Cut_Vowel/upload_form/vowel_cut/segmentation-kit/segment_julius.pl の49行目を①に合わせる
  ```perl:/Cut_Vowel/upload_form/vowel_cut/segmentation-kit/segment_julius.pl
  ## julius executable
  if ($^O =~ /MSWin/){
    $juliusbin=".\\bin\\julius-4.3.1.exe";
  } else {
    $juliusbin="/usr/local/bin/julius"; ##ココ
  }
  ```
  音響モデルを変更する場合は 53,54行目を編集 (monophoneの方が精度がいいらしい)
  ```perl:/Cut_Vowel/upload_form/vowel_cut/segmentation-kit/segment_julius.pl
  ## acoustic model
  $hmmdefs="./models/hmmdefs_monof_mix16_gid.binhmm";# monophone model
  #$hmmdefs="./models/hmmdefs_ptm_gid.binhmm"; # triphone model
  ```

4. サーバの起動方法，webアプリアクセス方法およびサーバ停止方法  
    Cut_Vowel ディレクトリに移動して開発サーバーを起動  
    - ローカルPC  
      - サーバ起動: `python3 manage.py runserver`  
      - アクセスURL:`localhost:8000`  
      - サーバ停止: Ctr + c
    - ローカルネットワークサーバ  
      - サーバ起動: `python3 manage.py runserver 0.0.0.0:8000`  
      ログアウトしてもバックグラウンドで動かす場合は  
      `nohup python3 manage.py runserver 0.0.0.0:8000 &`  
      - アクセスURL: `[サーバのIPアドレス]:8000`  
      - バックグラウンドを終了するときは  
        `ps aux | grep python3`  
        python3が動いているプロセス番号を確認し  
        `kill [プロセス番号]`

管理者ページのURL
`[localhost or サーバのIPアドレス]:8000/admin`
