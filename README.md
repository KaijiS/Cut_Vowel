# Cut_Vowel

**音素ラベリングセグメンテーションを用いた母音波形抽出webアプリ**

## 開発環境  
- OS: ubuntu  
- 使用したOSS: Julius  
- 開発言語:
  - perl(Julius内)
  - python3
- 必要なライブラリ:
  - numpy
  - scipy
  - Django(ウェブアプリケーションフレームワーク)

## 環境構築，サーバ起動方法およびwebアプリアクセス方法(Ubuntu16.04)  
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
/usr/local/bin/julius があることを確認

3. 本アプリをクローン  
webアプリ用ディレクトリで  
`git clone https://github.com/KaijiS/Cut_Vowel`  
 /Cut_Vowel/upload_form/vowel_cut/segmentation-kit/segment_julius.pl の49行目を編集
  ```perl:/Cut_Vowel/upload_form/vowel_cut/segmentation-kit/segment_julius.pl
  ## julius executable
  if ($^O =~ /MSWin/){
    $juliusbin=".\\bin\\julius-4.3.1.exe";
  } else {
    $juliusbin="./bin/julius-4.3.1";  →  $juliusbin="/usr/local/bin/julius";
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
