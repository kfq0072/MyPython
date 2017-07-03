#!/usr/bin/python
#-*- coding: utf-8 -*-
#encoding=utf-8 
import urllib2
import urllib
import os
from BeautifulSoup import BeautifulSoup
def getMyImageLink():
    html = urllib2.urlopen('http://www.dbmeinv.com/').read()
    soup = BeautifulSoup(html)

    liResult = soup.findAll('li',attrs={"class":"span3"})

    for li in liResult:
        imageEn = li.findAll('img')
        for image in imageEn:
            link = image.get('src')
            imageName = image.get('title')
            filePath = '/Users/hsm/AI/avImage/%s.png' %imageName
            urllib.urlretrieve(link,filesavepath)
            print filesavepath


if __name__ == '__main__':
    getMyImageLink()