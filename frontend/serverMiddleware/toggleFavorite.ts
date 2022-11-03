import { Client } from '@notionhq/client'
import url from 'url'
const notion = new Client({auth: process.env.NOTION_TOKEN_FEED})

module.exports = ({req, res}: {req: any, res: any}) => {
  req.query = url.parse(req.url, true).query
  const pageId = req.query.pageId;
  const isFavorite = req.query.newVal;

  (async () => {
    await notion.pages.update({
      page_id: pageId,
      properties: {
        favorite: {
          checkbox: JSON.parse(isFavorite.toLowerCase())
        },
      }
    })
  })()
}