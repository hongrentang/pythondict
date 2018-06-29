#coding:utf-8
from selenium import webdriver
import re

def parse(html,):
    parterne='<div class="bd" id=\"pageNo-\d+\".*?>(.*?)</div>'
    content = re.findall(parterne,html,re.S)
    texts=[]
    for text in content:
        text = re.sub('<.*?>|&nbsp;','',text)
        texts.append(text)
    return texts



def spider(url,filename):
    driver = webdriver.PhantomJS()
    url = url
    driver.get(url)
    html = driver.page_source
    texts = parse(html)
    with open(filename,'a') as f:
        for text in texts:
            f.write(text)



if __name__=='__main__':
    url = 'https://wenku.baidu.com/view/7dc9981ab7360b4c2e3f6444.html?sxts=1530264004619'
    filname = '2.txt'
    spider(url,filname)