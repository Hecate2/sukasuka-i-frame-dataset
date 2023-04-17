#### How to build your dataset

Place your files like this

```
sukasuka-i-frame-dataset:
  get_i_frames.py
  (Others...)
[MH&Airota&FZSD&VCB-Studio] Shuumatsu Nani Shitemasuka？ Isogashii Desuka？ Sukutte Moratte Ii Desuka？ [Ma10p_1080p]:
  [MH&Airota&FZSD&VCB-Studio] sukasuka [01][Ma10p_1080p][x265_flac_aac].mkv
  (Others...)
```

In the Python file I am just building `ffmpeg` commands for you. For Windows users, just try to install `ffmpeg` (make sure you include it in your system `Path`!) and then double-click `get_i_frames.bat`. 