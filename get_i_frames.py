import os
import re
import sys

VIDEO_PATH = "../[MH&Airota&FZSD&VCB-Studio] Shuumatsu Nani Shitemasuka？ Isogashii Desuka？ Sukutte Moratte Ii Desuka？ [Ma10p_1080p]"
OUTPUT_PATH = "i-frame-output"
IMAGE_FORMAT = '.webp'

if not os.path.exists(OUTPUT_PATH):
    os.mkdir(OUTPUT_PATH)
if os.listdir(OUTPUT_PATH):
    print(f"WARNING: OUTPUT_PATH {OUTPUT_PATH} not empty", file=sys.stderr)

all_videos_path = [s for s in os.listdir(VIDEO_PATH) if s.endswith(".mkv")]
print(all_videos_path)
assert len(all_videos_path) == 12
for s in all_videos_path:
    assert re.search(r"\[MH&Airota&FZSD&VCB-Studio] sukasuka \[\d{2}]\[Ma10p_1080p]\[x265_flac_aac]\.mkv", s)
all_videos_path = [os.path.join(VIDEO_PATH, s) for s in all_videos_path]

print('chcp 65001')
for i, v_path in enumerate(all_videos_path):
    cmd = rf'''start ffmpeg -skip_frame nokey -i "{v_path}" -sn -vsync vfr "./{OUTPUT_PATH}/[{str(i+1).zfill(2)}][%%03d]{IMAGE_FORMAT}" '''
    print(cmd)
    # print(os.system(cmd))
