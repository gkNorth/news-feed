<template>
  <div>
    <div class="grid grid-cols-2 gap-y-2 gap-x-5 mt-3 md:mt-16 md:grid-cols-3 px-6">
      <Card
        v-for="feed in filteredFeedsBySite"
        :key="feed.id"
        :feed="feed"
      />
    </div>
    <div class="fixed bottom-1 right-1 flex justify-center align-middle p-3 bg-gray-600 opacity-80 rounded">
      <a
        :href="`${getSiteUrl.url}`"
        class="text-base font-semibold hover:underline text-white"
        target='_blank'
        rel='noreferrer nofollow noopener'
      >
        {{getSiteUrl.site_title}}
      </a>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import { Feed, Site } from 'types'
import Card from '~/components/Card.vue'

export default Vue.extend({
  name: 'IndexPage',
  components: {
    Card,
  },
  computed: {
    filteredFeedsBySite(): Feed[] {
      return this.$store.getters.feeds.filter(
        (feed: Feed) => feed.site_title === this.$route.params.site
      )
    },
    getSiteUrl(): Site {
      return this.$store.getters.sites.find(
        (site: Site) => site.site_title === this.$route.params.site
      )
    }
  }
})
</script>
