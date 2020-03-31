# -*- coding: UTF-8 -*-

import requests
import urllib.request
from bs4 import BeautifulSoup
import os
import time


url = 'https://pixabay.com/zh/images/search/'
URL = 'https://pixabay.com/zh/images/search/'
headers = {'User-Agent': 'User-Agent:Mozilla/5.0'}
ind = 1
page = 1

for i in range(2, 100):
	response = requests.get(url, headers=headers)
	soup = BeautifulSoup(response.content, 'html.parser')
	items = soup.find_all('img')
	folder_path = './pics/'
	if os.path.exists(folder_path) == False:  # 判断文件夹是否已经存在
		os.makedirs(folder_path)  # 创建文件夹
	
	for index, item in enumerate(items):
		if item:		
			srcstr = item.get('src')
			if srcstr == "/static/img/blank.gif":
				srcstr = item.get('data-lazy')
			print("Downloading Pic", ind)
			html = requests.get(srcstr)   # get函数获取图片链接地址，requests发送访问请求
			img_name = folder_path + str(ind) +'.png'
			with open(img_name, 'wb') as file:  # 以byte形式将图片数据写入
				file.write(html.content)
				file.flush()
			file.close()  # 关闭文件
			print("Pic", ind, "Download Completed")
			ind += 1
			time.sleep(1)  # 自定义延时
			if ind % 100 == 0:
				break
	page += 1
	url = URL + "?pagi=" + str(page)
	print(url)

print('抓取完成')