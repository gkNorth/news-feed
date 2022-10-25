import os
from dotenv import load_dotenv
import libs.NotionDB as NDB
import libs.Scrape as SC

load_dotenv()

SITE = NDB.Site(os.environ['NOTION_TOKEN_SITE'], os.environ['DB_NEWS_SITE'])
sites = SITE.getValues()
FEED = NDB.Feed(os.environ['NOTION_TOKEN_FEED'], os.environ['DB_NEWS_FEED'])
feeds = FEED.getValues()

# スクレイピングするサイト情報を配列に格納
newsSite = []
for site in sites:
    siteTitle = site['properties']['site_title']['title'][0]['plain_text'] if len(site['properties']['site_title']['title']) else ''
    url = site['properties']['url']['rich_text'][0]['plain_text'] if len(site['properties']['url']['rich_text']) else ''
    path = site['properties']['path']['rich_text'][0]['plain_text'] if len(site['properties']['path']['rich_text']) else ''
    listTag = site['properties']['list_tag']['rich_text'][0]['plain_text'] if len(site['properties']['list_tag']['rich_text']) else 'ul'
    itemTag = site['properties']['item_tag']['rich_text'][0]['plain_text'] if len(site['properties']['item_tag']['rich_text']) else 'li'
    anchorTag = site['properties']['anchor_tag']['rich_text'][0]['plain_text'] if len(site['properties']['anchor_tag']['rich_text']) else 'a'
    imgTag = site['properties']['img_tag']['rich_text'][0]['plain_text'] if len(site['properties']['img_tag']['rich_text']) else 'img'
    pageTitleTag = site['properties']['page_title_tag']['rich_text'][0]['plain_text'] if len(site['properties']['page_title_tag']['rich_text']) else ''
    linkType = site['properties']['link_type']['number']
    dateTag = site['properties']['date_tag']['rich_text'][0]['plain_text'] if len(site['properties']['date_tag']['rich_text']) else ''

    newsSite.append(
        SC.ScrapeNews(
            siteTitle = siteTitle,
            url = url,
            path = path,
            listTag = listTag,
            itemTag = itemTag,
            anchorTag = anchorTag,
            imgTag = imgTag,
            pageTitleTag = pageTitleTag,
            linkType = linkType,
            dateTag = dateTag
        )
    )

# 既に登録されてるニュースのページリンクを格納する
validateNewsList = []
for feed in feeds:
    validateNewsList.append(feed['properties']['page_link']['rich_text'][0]['plain_text'])

# スクレイピングした情報を格納する
scrapeNewsList = []
for site in newsSite:
    newsList = site.getNews()
    for news in newsList:
        scrapeNewsList.append(news)

# DB情報とスクレイピング情報でページリンクが一致した要素のインデックスを抽出
removeNewsIndex = []
for i, scrapeNews in enumerate(scrapeNewsList):
    for validateNews in validateNewsList:
        if (scrapeNews['pageLink'] == validateNews):
            removeNewsIndex.append(i)

# 重複している要素をリストから削除する
for removeNews in reversed(removeNewsIndex):
    for i, scrapeNews in enumerate(scrapeNewsList):
        if i == removeNews:
            scrapeNewsList.remove(scrapeNews)

# DBに情報を格納する
for scrapeNews in scrapeNewsList:
    FEED.postFeed(scrapeNews['pageTitle'], scrapeNews['pageLink'], scrapeNews['pageImg'], scrapeNews['siteTitle'])
    print(scrapeNews['pageTitle'])


finishedMessage = '{}件の更新がありました'.format(len(scrapeNewsList)) if len(scrapeNewsList) > 0 else '更新はありませんでした'
print(finishedMessage)

# for registerNews in registerNewsList:
#     FEED.postFeed(registerNews['pageTitle'], registerNews['pageLink'], registerNews['pageImg'], registerNews['siteTitle'])

# scrapedNews = SCRAPENEWS.getNews()

# pprint(sites)

# newsTitle = SC.scrapeNews()

# libs.feed.postFeed(newsTitle)