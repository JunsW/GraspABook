#encoding:UTF-8

import urllib.request
import urllib.parse
import re
import os
from bs4 import BeautifulSoup
from retrying import retry
#import HTMLParser
bookNumber = '401'
filePathDir = os.getcwd() + '/Documents/Python/learning/contentBQG/contents/'

class fictionSpider:

    def __init__(self,startFlag=1):
        global bookNumber
        self.url = 'http://m.biquge.la/booklist/'+bookNumber+'.html'

        self.host = 'http://m.biquge.la'
        self.startFlag = startFlag
    
    def fetchPages(self):
        f = urllib.request.urlopen(url=self.url,timeout=120)
        return f.read()

#    def getPage(self,pageIndex):
#        url = self.siteURL + "?page=" + str(pageIndex)
#        request = urllib2.Request(url)
#        response = urllib2.urlopen(request)
#        return response.read().decode('gbk')

    def saveBrief(self,content,name):
        global filePathDir
        filePath = filePathDir+ name +".txt"
        f = open(filePath,"wb+")
        print("正在保存目录信息")
        print('='*40)
        f.write(content)
        f.close()
    
    def getFetchedContent(self):
        filePath = os.getcwd()+'/Documents/Python/learning/contentBQG/contents/'+"content.txt"
        f = open(filePath,"rb+")
        content = f.read()
        return content

    def extractEpisodeInfo(self,strToSearch,fileName):
        global bookNumber
        print("正在提取内容")
        print('='*40)
        hrefs = []
        rowTitles = []
        titles = []
        episodes = []
        phref = re.compile('\/book\/'+bookNumber+'/[0-9]*\.html')
#        pTitle = re.compile('第.+章.*<\/a')
        pTitle = re.compile('>.*<\/a')
        pEpisodes = re.compile('href.*book.*a>')
        
#        hrefs = phrefs.findall(strToSearch)
#        rowTitles = pTitles.findall(strToSearch)

        episodes = pEpisodes.findall(strToSearch)
        print(episodes[0])

        for episode in episodes:
            hrefs.append(phref.findall(episode)[0])
            titles.append(pTitle.search(episode).group()[1:-3])

        hrefs.reverse()
        titles.reverse()

        print('hrefs Fetched!')
        print('Titiles Fetched')
        self.fetchEpisodeContent(hrefs=hrefs,titles=titles,startFlag=self.startFlag,fileName=fileName)

    def fetchEpisodeContent(self,hrefs,titles,startFlag,fileName):
        index = 0
        for href in hrefs:
            if index < startFlag-1:
                index = index + 1
                continue
            print('Fetching the content ' + titles[index] + ' from ' + self.host + hrefs[index])
            url = self.host + hrefs[index]
            content = self.readPage(url) #===
#            content = self.removeTitleInContent(content) #===
            content = self.replaceBr(content) #===
            content = self.removeHTMLLabel(content) #===
            content = self.soupToString(content)
            
            self.savePage(fileName=fileName, content=content, title=titles[index].encode('utf-8')) #===
            
            index = index + 1
        else:
            print('Update to the episode: ',end='')
            print(index)

            
    def savePage(self,fileName,content,title):
        global filePathDir
        filePath = filePathDir + fileName +".txt"
        f = open(filePath,"ab+")
        f.write('###'.encode('utf-8')+title)
        f.write('\r'.encode('utf-8'))
        f.write(content)
        f.write('\r'.encode('utf-8')*2)


    @retry(stop_max_attempt_number=5)
    def readPage(self, url):
        f = urllib.request.urlopen(url=url,timeout=60)
        return f.read().decode('gbk')

    def removeTitleInContent(self,content):
        p = re.compile('第.+章<br\s\/>')
        content = p.sub('',content)
        return content

    def replaceBr(self,content):
        p = re.compile('<br\s\/>')
        content = p.sub('\n', content)
        return content

    def removeHTMLLabel(self,content):
        soup = BeautifulSoup(content)
        divContent = soup.select('div#nr1')
        return divContent
    def soupToString(self,content):
        content=content[0].text.encode('utf-8')
        return content[10:]

spider = fictionSpider(startFlag=1)##1199
resultA=spider.fetchPages()
##print(resultA)
spider.saveBrief(content=resultA,name='content')
str = spider.getFetchedContent()
spider.extractEpisodeInfo(str.decode('gbk'),fileName='frxxz')
##spider.extractEpisodeInfo(str)
#
#
















