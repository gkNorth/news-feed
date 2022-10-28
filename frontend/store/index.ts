import { IndexState, Feed } from 'types'
import { MutationTree, GetterTree, ActionTree } from 'vuex'
import { Client } from '@notionhq/client';
import dayjs from 'dayjs';

export const state = (): IndexState => ({
  feeds: [] as Feed[],
})

export type RootState = ReturnType<typeof state>

export const getters: GetterTree<IndexState, RootState> = {
  feeds: state => state.feeds,
}

export const mutations: MutationTree<IndexState> = {
  setFeeds(state: IndexState, feeds: Feed[]): void {
    state.feeds = feeds
  },
}

export const actions: ActionTree<IndexState, RootState> = {
  async fetchFeeds({ commit }) {
    const notion = new Client({ auth: process.env.NOTION_TOKEN_FEED || '' })
    const res = await notion.databases.query({
      database_id: process.env.DB_NEWS_FEED || '',
    })
    const feeds: Feed[] = res.results.map( (feed: any) => {
      return {
        id: feed.id,
        page_title: feed.properties.page_title.title[0].text.content,
        page_link: feed.properties.page_link.rich_text[0].plain_text,
        page_img: feed.properties.page_img.rich_text[0].plain_text,
        site_title: feed.properties.site_title.rich_text[0].plain_text,
        created_at: dayjs(feed.created_time).format("YYYY-MM-DD")
      }
    })
    commit('setFeeds', feeds)
  },
}