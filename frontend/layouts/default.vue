<template>
  <div>
    <TheHeader />
    <section class="bg-white dark:bg-gray-900">
      <div class="container mx-auto">
        <SiteSlide :sites=getSiteTitles />
        <!-- <h1 class="text-3xl font-semibold text-gray-800 capitalize lg:text-4xl dark:text-white">From the blog</h1> -->
        <div
          v-touch:swipe.right="() => $router.push(prevSite)"
          v-touch:swipe.left="() => $router.push(nextSite)"
        >
          <nuxt />
        </div>
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
    ...mapGetters(['feeds', 'sites']),
    getSiteTitles() {
      return this.feeds.filter(
        ( feed, index, self ) => self.findIndex(( key ) => key.site_title === feed.site_title) === index
      ).map(feed => feed.site_title)
    },
    currentPageIndex(): number {
      return this.getSiteTitles.findIndex(site => site === this.$route.params.site)
    },
    prevSite() {
      return this.currentPageIndex > 0 ? this.getSiteTitles[this.currentPageIndex - 1] : '/'
    },
    nextSite() {
      return this.currentPageIndex < this.getSiteTitles.length - 1 ? this.getSiteTitles[this.currentPageIndex + 1] : '/'
    },
  }
})
</script>