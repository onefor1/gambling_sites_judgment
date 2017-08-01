#!/usr/bin/python
# -*- coding:utf-8 -*-

import re
import requests
import chardet

patterns = [
    u'<title>(.*?)</title>', #获取网站的title
    u'title="([\u4e00-\u9fa5 0-9a-zA-Z]+)"', #获取网站的title
    u'"keywords" content="(.*?)"', #获取网站的keywords
    u">([a-zA-Z\u4e00-\u9fa5]{4,})<" #获取网站的主体内容
]

def getTextFromUrl(url):
    line = ""
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
            #"Accept-Language":"zh-CN,zh;q=0.8",
            "Connection": "keep-alive"
        }
        response = requests.get(url, headers=headers).content
        encoding = get_encoding(response)
        content = response.decode(encoding, 'ignore')
        
        for pattern in patterns:
            match = re.findall(pattern, content)
            if match:
                line += ",".join(match)
    except Exception, e:
        pass
    return line

def get_encoding(content):
    encoding_dict = chardet.detect(content)
    return encoding_dict["encoding"]
    