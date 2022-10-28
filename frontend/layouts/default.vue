<template>
  <div>
    <TheHeader />
    <section class="bg-white dark:bg-gray-900">
      <div class="container mx-auto">
        <SiteSlide :sites=getSiteTitles />
        <!-- <h1 class="text-3xl font-semibold text-gray-800 capitalize lg:text-4xl dark:text-white">From the blog</h1> -->
        <nuxt />
      </div>
    </section>
    <TheFooter />
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import { mapGetters } from 'vuex'
import TheHeader from '~/components/TheHeader.vue'
import TheFooter from '~/components/TheFooter.vue'
import Card from '~/components/Card.vue'
import SiteSlide from '~/components/SiteSlide.vue'

export default Vue.extend({
  components: {
    Card,
    SiteSlide,
    TheHeader,
    TheFooter,
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