import os
import datetime
import shutil

now = datetime.datetime.now()
today = str(now.year)+'-'+str(now.month)+'-'+str(now.day)

newfilepath = r'C:\\Users\\dfunai\\Pictures\\画面キャプチャ\\'+ today
print('生成されたフォルダ：' + newfilepath)

filepath = r'C:\\Users\\dfunai\\Pictures\\画面キャプチャ\\tmp'
shutil.move(filepath, newfilepath)
print('移動しました')

os.mkdir(filepath)
print('生成されたフォルダ２：' + filepath)
