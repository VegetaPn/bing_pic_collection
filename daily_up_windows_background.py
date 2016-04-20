# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
import datetime
import time
from PIL import Image
import win32gui
import win32con
import win32api

import collect_pics


# convert jpg to bmp
def set_wall_paper_from_jpg(image_path):
	bmpImage = Image.open(image_path)
	newPath = image_path.replace('.jpg', '.bmp')
	bmpImage.save(newPath, "BMP")
	set_wall_paper_from_bmp(newPath)


def set_wall_paper_from_bmp(image_path):
	k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
	win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "2")  # 2拉伸适应桌面,0桌面居中
	win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
	win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, image_path, 1+2)
	os.remove(image_path)


def timer_to_up_background(schedule_time):
	while(True):
		print(datetime.datetime.now().strftime('%Y-%m-%d %X')+'>>>> Bing Paper Running...')
		nowa_date = datetime.datetime.now().strftime('%Y%m%d')
		try:
			collect_pics.collect_bing_picure()
			set_wall_paper_from_jpg(collect_pics.COLLECTION_DIR + nowa_date + '.jpg')
			print('Windows background changed successful')
			time.sleep(schedule_time)
		except Exception as e:
			print(e)
			time.sleep(60)


if __name__ == '__main__':
	timer_to_up_background(8*60*60)

# set_wall_paper_from_jpg('wall_papers/20160418.jpg')