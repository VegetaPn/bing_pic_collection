# -*- coding: utf-8 -*-

import urllib
import datetime

COLLECTION_DIR = 'collection/images/'


def collect_bing_picure():
	pic_url = None
	f = urllib.urlopen('http://cn.bing.com/')
	page_source = str(f.read())

	if page_source.find('http://s.cn.bing.net/') >= 1:
		pre_url = page_source.split('http://s.cn.bing.net')[1]
		clean_url = pre_url.split('.jpg')[0]
		pic_url = 'http://s.cn.bing.net%s.jpg' % clean_url
		print(pic_url)

	if pic_url is not None:
		nowa_time = datetime.datetime.now().strftime('%Y%m%d')
		urllib.urlretrieve(pic_url, COLLECTION_DIR + nowa_time + '.jpg')
		print('download successful')


if __name__ == '__main__':
	collect_bing_picure()