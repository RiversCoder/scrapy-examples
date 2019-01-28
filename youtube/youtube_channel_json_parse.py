# url: https://www.youtube.com/channel/UCNkaVZyk8KATLCioC7iQx5A/videos
# 
#encoding=utf-8
from selenium import webdriver  
import time  
import os
from bs4 import BeautifulSoup
import json
import requests
from contextlib import closing

channel_url = 'https://www.youtube.com/channel/UCNkaVZyk8KATLCioC7iQx5A/videos'
json_path = './Animals Channel TV.json'
D_PATH = 'D:\\videos\\youtube动物\\'

class ChannelInfo:
	def __init__(self):
		self.title = ''
		self.playCount = ''
		self.publishTime = ''
		self.cover = ''
		self.duration = ''
		self.videoUrl = ''
		self.author = ''
	pass

cinfoSchema = {
	'title': '', 
	'playCount': '',
	'publishTime': '',
	'cover': '',
	'duration': '',
	'videoUrl': '',
	'author': ''
}


class GetChannelVideoByJson:

	def __init__(self, url):

		self.channel_url = url
		self.channel_videos = []
		

	def getRequest(self):
		self.driver = webdriver.Firefox()
		time.sleep(3)
		self.driver.get(r''+ self.channel_url)
		script = 'let aaaa_timer = setInterval(function(){\
			document.documentElement.scrollTop += 100\
		},100);\
		setTimeout( function(){\
			clearInterval(aaaa_timer)\
		}, 6000 ) ';
		self.driver.execute_script(script)
		time.sleep(3)

		results = self.driver.find_elements_by_css_selector("#items ytd-grid-video-renderer")
		self.channel_videos = []

		for result in results:
			links = result.find_element_by_xpath(".//h3/a")
			img = result.find_element_by_xpath(".//img")
			count = result.find_element_by_xpath(".//div[@id='metadata-line']//span[1]")
			ptime = result.find_element_by_xpath(".//div[@id='metadata-line']//span[last()]")
			#duration = result.find_element_by_xpath(".//div[@id='overlays']//span")

			print('\n')
			print('作者：'+ self.driver.find_element_by_xpath("//span[@id='channel-title']").text )
			print('标题：'+ links.text)
			print('链接：'+ links.get_attribute('href'))
			print('封面:'+ str(img.get_attribute('src')))
			print('播放:'+ count.text)
			print('发布:'+ ptime.text)
			print('\n')

			self.channel_videos.append({
				'title': links.text, 
				'playCount': count.text,
				'publishTime': ptime.text,
				'cover': str(img.get_attribute('src')),
				'duration': '',
				'videoUrl': links.get_attribute('href'),
				'author': self.driver.find_element_by_xpath("//span[@id='channel-title']").text
			})

		# 替换所有的视频下载链接且同步下载
		self.getDonwloadHref();
	
	# 通过第三方网站下载youtube视频		
	def getDonwloadHref(self):
		
		# 'https://qdownloader.net/download?video=https://www.youtube.com/watch?v=vhd7afdwL00'
		for it in self.channel_videos:
			it['videoUrl'] = self.parseDownUrl(it['videoUrl'])
			print(it['videoUrl'])
			print(self.channel_videos.index(it))
		
		# 写入JSON文件
		with open(self.channel_videos[0]['author']+'.json','w') as file_object:
			json.dump(self.channel_videos, file_object)

			
		# 在指定目录批量下载头图和文件
		for it in self.channel_videos:
			#下载图片
			self.downloads(it['videoUrl'], D_PATH+'video\\'+it['title']+'.mp4')
			#下载视频
			self.downloads(it['cover'].split('?')[0], D_PATH+'image\\'+it['title']+'.jpg')	


	# 通过第三方网站下载youtube视频		
	def getDonwloadHrefByJson(self, json_path):
		# self.driver = webdriver.Firefox()
		# time.sleep(2)
		with open(json_path, encoding='utf-8') as file:
			content = json.load(file)
			for it in content[1:]:
				#self.driver.get(r''+it['videoUrl'])
				#time.sleep(1);
				#print(content.index(it))
				#下载视频
				self.downloads(it['videoUrl'], D_PATH+'video\\'+it['title']+'.mp4')
				#下载图片
				#self.downloads(it['cover'].split('?')[0], D_PATH+'image\\'+it['title']+'.jpg')	


	def downloads(self, file_url, new_file_path):
		print(file_url)
		headers = { "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36" }
		proxy = { "https": "socks5://127.0.0.1:1080", "http": "socks5://127.0.0.1:1080" } 
		with closing(requests.get(file_url, headers=headers, proxies=proxy,  stream=True)) as response:
			chunk_size = 1024  # 单次请求最大值
			content_size = (int(response.headers['content-length'])/chunk_size/chunk_size)  # 内容体总大小
			data_count = 0
			print('\n开始下载:\n')
			# 创建目录
			self.mkdir(file_url)
			# 开始下载操作
			#D_PATH + self.data['file_name'] + '.mp4'
			with open(new_file_path, 'wb') as file:
				for data in response.iter_content(chunk_size = chunk_size):
					file.write(data)
					data_count += (len(data)/chunk_size/chunk_size)
					now_progress = (data_count / content_size) * 100
					print("\r 文件下载进度：%d%%(%d M/%d M) - %s " % (now_progress, data_count, content_size, self.data['file_name']), end=" ")
			print('\n\n下载成功!\n')		


	def parseDownUrl(self, url):
		parseUrl = 'https://qdownloader.net/download?video='
		self.driver.get(r''+parseUrl+ url)
		time.sleep(1)
		href = self.driver.find_element_by_xpath("//table[@class='downloadsTable']//tbody//tr[1]//a[1]").get_attribute('href')
		return href


	def mkdir(self, path):

		# 去除首位空格
		path = path.strip()
		# 去除尾部 \ 符号
		path = path.rstrip("\\")

		# 判断路径是否存在
		isExists = os.path.exists(path)

		# 判断结果
		if not isExists:
			os.makedirs(path)
			return True
		else:
			return False

	pass





cv = GetChannelVideoByJson(channel_url)
cv.getDonwloadHrefByJson(json_path)
