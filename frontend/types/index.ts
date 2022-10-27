export interface IndexState {
  feeds: Feed[]
}

export interface Feed {
  id: number
  page_title: string
  page_link: string
  page_img: string
  site_title: string
}