import os
import datetime
import shutil
import sys
from PIL import ImageGrab

today = datetime.datetime.now().strftime('%Y-%m-%d')
today_file = 'ScreenCapture_' + today
now = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')

today_file = 'ScreenCapture_' + today

if not os.path.exists(today_file):
    os.mkdir(today_file)

ImageGrab.grab().save(today_file + '/' + now + '.png')
