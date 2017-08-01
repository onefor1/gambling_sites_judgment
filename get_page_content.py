#coding=utf-8
import requests
import re
import random
import time
import chardet

#words = [u"聚博", u"真人娱乐", u"电子游艺", u"威尼斯人", u"彩票", u"博菜", u"六合彩", u"特码", u"中特", u"老虎机", u"投注", u"博彩"]
'''
博彩网站一般开发没有统计的规范，所以正则难以统一
但是博彩网站一般为了贴近浏览器，会在title, keywords给出博彩相关的关键词
博彩网站还存在于菜单和正文内容中，但是采用的标签都不一样，但是基本都可以使用r">([a-zA-Z\u4e00-\u9fa5]{4,})<"将内容取出
'''
patterns = [
	u'<title>(.*?)</title>', #获取网站的title
	u'title="([\u4e00-\u9fa5 0-9a-zA-Z]+)"', #获取网站的title
	u'"keywords" content="(.*?)"', #获取网站的keywords
	u">([a-zA-Z\u4e00-\u9fa5]{4,})<" #获取网站的主体内容
]

def get_encoding(content):
	'''
	判定网页的编码
	'''
	encoding_dict = chardet.detect(content)
	return encoding_dict["encoding"]

def get_content(url):
	'''
	获取页面内容
	'''
	try:
		headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
			#"Accept-Language":"zh-CN,zh;q=0.8",
			"Connection": "keep-alive"
		}
		#response = requests.get("http://" + url, headers=headers).content
		response = requests.get(url, headers=headers).content

		encoding = get_encoding(response)
		content = response.decode(encoding, 'ignore')
		#print content
		#保存原始网页内容
		# save_file1 =  time.strftime("%Y%m%d", time.localtime()) + "_" + url.split("/") + ".txt"
		# with open("original_data/" + save_file1, "w+") as file1:
		# 	file1.write(content.encode("utf-8"))
		# 	file1.flush()

		line = ""
		for pattern in patterns:
			match = re.findall(pattern, content)
			if match:
				line += ",".join(match)
		if match:
			line += ','.join(match)

		#保存提取之后的页面内容
		#save_file2 =  time.strftime("%Y%m%d", time.localtime()) + "_" + str(random.random()) + ".txt"
		#save_file2 = time.strftime("%Y%m%d", time.localtime()) + "_" + url + ".txt"
		save_file2 = url.split("/")[-1]
		with open("data_news/" + save_file2, "w+") as file2:
			file2.write(line.encode("utf-8"))
			file2.flush()

		return line
	except Exception, e:
		print e


#url = "www.352206.cc"
#url = "9999kj.com"
#url = "jubo222.com"
#url = "news.ifeng.com/a/20151214/46658197_0.shtml"
#url = "finance.qq.com/a/20110718/001103.htm"
#print get_content(url)
count = 1
for url in open('urltest.txt', 'r'):
	print count, url
	get_content(url.strip())
	count += 1