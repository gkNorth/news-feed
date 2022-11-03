import { IndexState, Feed, Site } from 'types'
import { MutationTree, GetterTree, ActionTree, ActionContext } from 'vuex'
import { Client } from '@notionhq/client';
import dayjs from 'dayjs';

export const state = (): IndexState => ({
  feeds: [] as Feed[],
  sites: [] as Site[],
})

export type RootState = ReturnType<typeof state>

export const getters: GetterTree<IndexState, RootState> = {
  feeds: state => state.feeds,
  sites: state => state.sites,
}

export const mutations: MutationTree<IndexState> = {
  setFeeds(state: IndexState, feeds: Feed[]): void {
    state.feeds = feeds
  },
  updateFeed(state: IndexState, { favorite, targetFeed }): void {
    const target = state.feeds.find(feed => feed.id === targetFeed.id)
    if (!target) return
    target.favorite = favorite
  },
  setSites(state: IndexState, sites: Site[]): void {
    state.sites = sites
  },
}

export const actions: ActionTree<IndexState, RootState> = {
  nuxtServerInit: async (context: ActionContext<RootState, RootState>) => {
    let feeds: Feed[] = []
    const notionFeeds = new Client({ auth: process.env.NOTION_TOKEN_FEED || '' })
    const resFeeds = await notionFeeds.databases.query({
      database_id: process.env.DB_NEWS_FEED || '',
    })
    let hasMore = resFeeds.has_more
    let nextCursor = resFeeds.next_cursor
    const feedsItems: Feed[] = resFeeds.results.map( (feed: any) => {
      const emoji = createEmoji()
      return {
        id: feed.id,
        page_title: feed.properties.page_title.title[0].text.content,
        page_link: feed.properties.page_link.rich_text[0].plain_text,
        page_img: feed.properties.page_img.rich_text[0].plain_text,
        site_title: feed.properties.site_title.rich_text[0].plain_text,
        favorite: feed.properties.favorite.checkbox,
        created_at: dayjs(feed.created_time).format("YYYY-MM-DD"),
        emoji: emoji
      }
    })
    feeds = [...feeds, ...feedsItems]
    while (hasMore) {
      if (nextCursor === null) return
      const resFeeds = await notionFeeds.databases.query({
        database_id: process.env.DB_NEWS_FEED || '',
        start_cursor: nextCursor,
      })
      const feedsItems: Feed[] = resFeeds.results.map( (feed: any) => {
        const emoji = createEmoji()
        return {
          id: feed.id,
          page_title: feed.properties.page_title.title[0].text.content,
          page_link: feed.properties.page_link.rich_text[0].plain_text,
          page_img: feed.properties.page_img.rich_text[0].plain_text,
          site_title: feed.properties.site_title.rich_text[0].plain_text,
          favorite: feed.properties.favorite.checkbox,
          created_at: dayjs(feed.created_time).format("YYYY-MM-DD"),
          emoji: emoji
        }
      })
      feeds = [...feeds, ...feedsItems]
      hasMore = resFeeds.has_more
      nextCursor = resFeeds.next_cursor
    }
    feeds.sort((a, b) => (a.created_at < b.created_at ? 1 : -1))
    context.commit('setFeeds', feeds)
    
    const notionSites = new Client({ auth: process.env.NOTION_TOKEN_SITE || '' })
    const resSites = await notionSites.databases.query({
      database_id: process.env.DB_NEWS_SITE || '',
    })
    const sites: Site[] = resSites.results.map( (sites: any) => {
      return {
        id: sites.id,
        site_title: sites.properties.site_title.title[0].text.content,
        url: sites.properties.url.rich_text[0].plain_text,
        path: sites.properties.path.rich_text[0].plain_text,
        list_tag: sites.properties.list_tag.rich_text[0].plain_text,
        item_tag: sites.properties.item_tag.rich_text[0].plain_text,
        anchor_tag: sites.properties.anchor_tag.rich_text[0].plain_text,
        img_tag: sites.properties.img_tag.rich_text[0].plain_text,
        page_title_tag: sites.properties.page_title_tag.rich_text[0].plain_text,
        link_type: sites.properties.link_type.number,
        date_tag: sites.properties.date_tag.rich_text[0].plain_text,
        created_at: dayjs(sites.created_time).format("YYYY-MM-DD"),
      }
    })
    context.commit('setSites', sites)
  },
  updateFavorite(context, { favorite, targetFeed }) {
    context.commit('updateFeed', {favorite, targetFeed})
  }
}

export const createEmoji = () => {
  const emojiCode: number = 
    Math.random()*10 > 7.75 ? Math.floor(Math.random()) * (128592 - 128512) + 128512 : Math.floor(Math.random() * (128318 - 127744) + 127744)
  return String.fromCodePoint(emojiCode)
}