const { Client } = require("@notionhq/client")
// import { Client } from '@notionhq/client'
import { News } from 'types'

export default async function fetchProjects() {
  const notion: any = new Client({ auth: process.env.NOTION_TOKEN_FEED });
  const databaseId: any = process.env.DB_NEWS_FEED;
  const response: any = await notion.databases.query({ database_id: databaseId });
  
  const newsList: News[] = response.results.map((result: any, index: number) => (
    {
      id: index,
      pageTitle: result.properties.page_title.title[0].plain_text,
      pageLink: result.properties.page_link.rich_text[0].plain_text,
      pageImg: result.properties.page_img.rich_text[0].plain_text,
      siteTitle: result.properties.site_title.rich_text[0].plain_text,
      created_by: result.created_time,
    }
  ))
  
  return newsList
}