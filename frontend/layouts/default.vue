<template>
  <div>
    <section class="bg-white dark:bg-gray-900">
      <div class="container px-6 py-10 mx-auto">
        <SiteSlide :sites=getSiteTitles />
        <h1 class="text-3xl font-semibold text-gray-800 capitalize lg:text-4xl dark:text-white">From the blog</h1>

        <nuxt />
      </div>
    </section>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import { mapGetters } from 'vuex'
import Card from '~/components/Card.vue'
import SiteSlide from '~/components/SiteSlide.vue'

export default Vue.extend({
  components: {
    Card,
    SiteSlide,
  },
  async asyncData({ store }): Promise<void> {
    await store.dispatch('fetchFeeds')
  },
  computed: {
    ...mapGetters(['feeds']),
    getSiteTitles() {
      return this.feeds.filter(
        ( feed, index, self ) => self.findIndex(( key ) => key.site_title === feed.site_title) === index
      ).map(feed => feed.site_title)
    },
  }
})
</script>