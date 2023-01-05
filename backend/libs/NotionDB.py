from notion_client import Client
    
class NotionDB:
    def __init__(self, envToken, envDb):
        self.notion = Client(auth=envToken)
        self.db_id = envDb

    def getValues(self):
        feeds = []
        db = self.notion.databases.query(
            **{
                'database_id' : self.db_id
            }
        )
        feeds = [* db['results']]
        hasMore = db['has_more']
        nextCursor = db['next_cursor']
        # while hasMore:
        #     db = self.notion.databases.query(
        #         **{
        #             'database_id' : self.db_id,
        #             'start_cursor': nextCursor,
        #         }
        #     )
        #     feeds = [* feeds, * db['results']]
        #     hasMore = db['has_more']
        #     nextCursor = db['next_cursor']
        return feeds

class Feed(NotionDB):
    def __init__(self, envToken, envDb):
        super().__init__(envToken, envDb)

    def postFeed(self, pageTitle, pageLink, pageImg, siteTitle):
        self.notion.pages.create(
        **{
            'parent': {'database_id': self.db_id},
            'properties': {
                'page_title': {
                    'title': [
                        {
                            'text': {
                                'content': pageTitle
                            }
                        }
                    ]
                },
                'page_link': {
                    'rich_text': [
                        {
                            'text': {
                                'content': pageLink
                            }
                        }
                    ]
                },
                'page_img': {
                    'rich_text': [
                        {
                            'text': {
                                'content': pageImg
                            }
                        }
                    ]
                },
                'site_title': {
                    'rich_text': [
                        {
                            'text': {
                                'content': siteTitle
                            }
                        }
                    ]
                },
            }
        }
    )

class Site(NotionDB):
    def __init__(self, envToken, envDb):
        super().__init__(envToken, envDb)