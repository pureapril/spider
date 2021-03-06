# -*- coding:utf-8 -*-
# demo1 基础
# demo2 Beautiful Soup 
# demo3 多线程并发抓爬
'''
功能：从网页抓取数据
安装：pip install beautifulsoup4
	  pip install lxml   第三方html解析器lxml,妈的安装失败，再一次感受到win系统开发的垃圾之处
	  pip install html5lib  第三方html解析器lxml安不上，只能安这个了
'''
__author__ ="April"	 

from urllib import request
from urllib.error import URLError, HTTPError
from bs4 import  BeautifulSoup
import html5lib

#盗墓笔记下载爬虫类
class DMBJ(object):
 
	#初始化，传入基地址
	def __init__(self,baseUrl):
		self.url = baseUrl
		#初始化headers(referer用于反'防盗链')
		#防盗链：服务器通过识别headers中的referer是不是它自己，如果不是则不会响应的一种安全措施
		user_agent ="Mozilla/5.0 (Windows NT 5.1; rv:39.0) Gecko/20100101 Firefox/39.0"
		self.headers = { 'User-Agent' : user_agent,'Referer': baseUrl}
 
	def download(self):
		try:
			#构建一个request:req
			req = request.Request(self.url,headers=self.headers)
			response = request.urlopen(req)
			#print(response.read())		控制台查看
			html = response.read()
			return html
		except HTTPError as e:
			print('The server couldn\'t fulfill the request.')
			print('Error code: ', e.code)
		except URLError as e:
			print('We failed to reach a server.')
			print('Reason: ', e.reason)
		except Exception as e:
			print("Error:",e)

	# 通过beautifulsoup4 按照部(小说共八部书)筛选出小说 
	def searchBookByBlock(self,html):
		print("---------------begin---------------")
		soup = BeautifulSoup(html,"html5lib")
		#筛选出class="container"的所有div,class是python的关键字，所以这里加下划线
		title = soup.find('p')
		print(title)
		blocks = soup.findAll("div",class_="container")
		for block in blocks:

			aTags = block.findAll("a")
			for atag in aTags:
				print(atag.strings)
			self.saveFile2(title, block.strings)
			#print(blockTag.name)
			#
			#
		print("---------------end1---------------")
		block = blocks[0]
		# for tag in block.descendants:
			# print(tag.name)
		print("---------------end2---------------")

		print(block)
		return blocks[0]


	def saveFile(self,data):
		print("---------------保存---------------")
		save_path = 'D:\\盗墓笔记.txt'
		f_obj = open(save_path, 'wb') # wb 表示打开方式 
		f_obj.write(data)
		f_obj.close()

	def saveFile2(self,fileName,data):
		print("---------------保存---------------")
		save_path = 'C:\\Users\Alex\Desktop\python\\'+fileName+'.txt'
		f_obj = open(save_path, 'wb') # wb 表示打开方式
		f_obj.write(data)
		f_obj.close()
 
baseURL = 'http://www.nanpaisanshu.org/daomubiji/'
dmbj = DMBJ(baseURL)
html = dmbj.download()
data = dmbj.searchBookByBlock(html)
#for book in data:
	#print(str(book.content))
	#dmbj.saveFile(book.content)
