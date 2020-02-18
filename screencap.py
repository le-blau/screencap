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
save_path = sys.argv[1] + '/' + 'ScreenCapture_' + today

if not os.path.exists(save_path):
    os.mkdir(save_path)

ImageGrab.grab().save(save_path + '/' + file_name)
