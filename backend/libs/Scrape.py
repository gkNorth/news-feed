import requests
from bs4 import BeautifulSoup

class ScrapeNews:
    def __init__(self, siteTitle, url, path='', listTag='ul', itemTag='li', anchorTag='a',  imgTag='img', pageTitleTag='a', linkType=1, dateTag=''):
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

    def getNews(self):
        res = requests.get(self.url)
        soup = BeautifulSoup(res.text, 'html.parser')
        newsListHTML = soup.select(self.itemTag)
        newsList = []
        
        for el in newsListHTML:
            pageTitle = el.select_one(self.pageTitleTag).text
            pagePath = el.select_one(self.anchorTag).get('href') if el.select_one(self.anchorTag) != None else el.get('href')
            pageLink = pagePath if self.linkType == 1 else '{}{}'.format(self.url, pagePath)
            pageImg = el.select_one(self.imgTag).get('src') if el.select_one(self.imgTag) else ''

            newsList.append(
                {
                    'siteTitle' : self.siteTitle,
                    'pageTitle' : pageTitle,
                    'pageLink' : pageLink,
                    'pageImg' : pageImg,
                }
            )
        
        return newsList