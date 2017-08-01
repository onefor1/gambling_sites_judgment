#coding=utf-8
import multiprocessing
import os, time, random
import sys
import requests

'''
对获取的url链接进行筛选，筛选出高精度的博彩url给get_page_content.py使用
'''

def judge_url(url):
    #words = [u"聚博", u"威尼斯人", u"娱乐场", u"彩票", u"博菜", u"合彩", u"澳门", u"六合彩", u"老虎机", u"投注", u"博彩"]
    words = [u"聚博", u"真人娱乐", u"电子游艺", u"威尼斯人", u"彩票", u"博菜", u"六合彩", u"特码", u"中特", u"老虎机", u"投注", u"博彩"]
    #print url
    try:
        response = requests.get("http://" + url)
        #不采用状态码判定页面返回是否正常，原因；现在很多博彩页面返回状态404，但实际上返回了正常页面
        if len(response.content) < 3000:
            return False
        for word in words:
            if word in response.text:
                return True
    except Exception, e:
        pass

    return False

def handle_url(urls):
    while True:
        if not urls.empty():
            url = urls.get(False)
            if judge_url(url):
                print url
        else:
            break

def read_url(urls, filename):
    with open(filename, "r") as file:
        line = file.readline().strip()
        while line:
            #line = line.split("\t")
            #print "url", line[0]
            if len(line) < 30: #数据里面有污染数据
                urls.put(line)
            line = file.readline().strip()
 
if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    urls = multiprocessing.Queue()
    #filename = sys.argv[1]
    filename = "url_web_scan.txt"
    read_url(urls, filename)
    print "read url ok"
    print urls.qsize()

    p1 = multiprocessing.Process(target=handle_url, args=(urls,))
    p2 = multiprocessing.Process(target=handle_url, args=(urls,))
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    
    print
    print 'end'
