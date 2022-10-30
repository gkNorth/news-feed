import requests
from bs4 import BeautifulSoup
import feedparser

class ScrapeNews:
    def __init__(self, siteTitle, url, path='', listTag='ul', itemTag='li', anchorTag='a',  imgTag='img', pageTitleTag='a', linkType=1, dateTag='', feedType=''):
        self.siteTitle = siteTitle
        self.url = url
        self.path = path
        self.listTag = listTag
        self.itemTag = itemTag
        self.anchorTag = anchorTag
        self.imgTag = imgTag
        self.pageTitleTag = pageTitleTag
        self.linkType = linkType
        self.dateTag = dateTag
        self.feedType = feedType

    def getNews(self):
        if (self.feedType == 'rss'):
            rssData = feedparser.parse(self.path)
            newsList = []
            for el in rssData.entries:
                pageTitle = el.title
                pageLink = el.link
                newsList.append(
                    {
                        'siteTitle' : self.siteTitle,
                        'pageTitle' : pageTitle,
                        'pageLink' : pageLink,
                        'pageImg' : 'false',
                    }
                )
            return newsList
        elif (self.feedType == 'json'):
            res = requests.get(self.path)
            newsListHTML = res.json()
            newsList = []
            for el in newsListHTML['data']['notes']: #jsonサイト追加する場合dataを動的にする必要あるかも
                pageTitle = el['name']
                pageLink = el['note_url']
                pageImg = el['eyecatch']
                newsList.append(
                    {
                        'siteTitle' : self.siteTitle,
                        'pageTitle' : pageTitle,
                        'pageLink' : pageLink,
                        'pageImg' : pageImg,
                    }
                )
            return newsList
        else:
            res = requests.get(self.url)
            soup = BeautifulSoup(res.text, 'html.parser')
            newsListHTML = soup.select(self.itemTag)
            newsList = []
            
            for el in newsListHTML:
                pageTitle = el.select_one(self.pageTitleTag).text
                pagePath = el.select_one(self.anchorTag).get('href') if el.select_one(self.anchorTag) != None else el.get('href')
                pageLink = pagePath if self.linkType == 1 else '{}{}'.format(self.url, pagePath)
                pageImg = el.select_one(self.imgTag).get('src') if el.select_one(self.imgTag) else 'false'
                newsList.append(
                    {
                        'siteTitle' : self.siteTitle,
                        'pageTitle' : pageTitle,
                        'pageLink' : pageLink,
                        'pageImg' : pageImg,
                    }
                )
            return newsList