export interface IndexState {
  feeds: Feed[]
  sites: Site[]
}

export interface Feed {
  id: number
  page_title: string
  page_link: string
  page_img: string
  site_title: string
  favorite: boolean
  created_at: string
  emoji: string
}

export interface Site {
  id: number
  site_title: string
  url: string
  path: string
  list_tag: string
  item_tag: string
  anchor_tag: string
  img_tag: string
  page_title_tag: string
  link_type: number
  date_tag: string
  created_at: string
}