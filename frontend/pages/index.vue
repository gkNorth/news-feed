<template>
  <div>
    <div class="grid grid-cols-2 gap-y-2 gap-x-5 mt-3 md:mt-16 md:grid-cols-3 px-6">
      <Card
        v-for="feed in displayFeeds"
        :key="feed.id"
        :feed="feed"
      />
    </div>
    <client-only>
      <infinite-loading @infinite="infiniteHandler"></infinite-loading>
    </client-only>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import Card from '~/components/Card.vue'
import { Feed } from 'types'

export type Data = {
  allFeeds: Feed[]
  displayFeeds: Feed[]
}

export default Vue.extend({
  name: 'IndexPage',
  components: {
    Card,
  },
  data(): Data {
    return {
      allFeeds: [],
      displayFeeds: [],
    }
  },
  async asyncData({ store }): Promise<Data> {
    return {
      allFeeds: store.getters.feeds,
      displayFeeds: store.getters.feeds.slice(0, 10),
    }
  },
  methods: {
    addFeeds(): boolean {
      const nowFeedsLength: number = this.displayFeeds.length
      const addFeedsLength: number = this.displayFeeds.length + 10
      const addingFeeds: Feed[] = this.$store.getters.feeds.slice(nowFeedsLength, addFeedsLength)
      this.displayFeeds.push(...addingFeeds)
      return addingFeeds.length >= 10 ? true : false
    },
    infiniteHandler($state: any): void {
      setTimeout(() => {
        const hasFeeds = this.addFeeds()
        hasFeeds ? $state.loaded() : $state.complete()
      }, 500)
    },
  }
})
</script>
