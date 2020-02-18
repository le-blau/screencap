import os
import datetime
import sys
from PIL import ImageGrab

def check_input():
    if len(sys.argv) < 2:
        sys.exit("引数が足りません")

    if not os.path.isdir(sys.argv[1]):
        sys.exit("指定のディレクトリは存在しません")


today = datetime.datetime.now().strftime('%Y-%m-%d')
file_name = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S') + '.png'

check_input()
# 第1引数に保存先はディレクトリを指定
save_path = sys.argv[1] + '/' + 'ScreenCapture_' + today

if not os.path.exists(save_path):
    os.mkdir(save_path)

# キャプチャ
ImageGrab.grab().save(save_path + '/' + file_name)
