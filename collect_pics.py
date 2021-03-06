# -*- coding: utf-8 -*-

import os
import urllib
import datetime

COLLECTION_DIR = 'collection/images/'


def collect_bing_picure():
	pic_url = None
	f = urllib.urlopen('http://cn.bing.com/')
	page_source = str(f.read())
	f.close()

	if page_source.find('s.cn.bing.net') >= 1:
		pre_url = page_source.split('s.cn.bing.net')[1]
		clean_url = pre_url.split('.jpg')[0].replace('\\', '')
		pic_url = 'http://s.cn.bing.net%s.jpg' % clean_url
		print(pic_url)
	elif page_source.find('g_img={url: "') >= 1:
		pic_url = 'http://cn.bing.com' + page_source.split('g_img={url: "')[1].split('"')[0]
		print(pic_url)
	else:
		raise Exception('当前版本已过时，请升级版本或与开发者联系: https://github.com/VegetaPn/bing_pic_collection')

	if pic_url is not None:
		nowa_time = datetime.datetime.now().strftime('%Y%m%d')

		if not os.path.exists(COLLECTION_DIR):
			os.mkdir(COLLECTION_DIR)
		urllib.urlretrieve(pic_url, COLLECTION_DIR + nowa_time + '.jpg')

		print('download successful')


if __name__ == '__main__':
	collect_bing_picure()
