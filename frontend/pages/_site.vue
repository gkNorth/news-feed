<template>
  <div class="grid grid-cols-2 gap-8 mt-8 md:mt-16 md:grid-cols-3">
    <Card
      v-for="feed in filteredFeedsBySite"
      :key="feed.id"
      :feed=feed
    />
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import { mapGetters } from 'vuex'
import Card from '~/components/Card.vue'

export default Vue.extend({
  name: 'IndexPage',
  components: {
    Card,
  },
  async asyncData({ store }): Promise<void> {
    await store.dispatch('fetchFeeds')
  },
  computed: {
    ...mapGetters(['feeds']),
    filteredFeedsBySite() {
      return this.$store.getters.feeds.filter(
        feed => feed.site_title === this.$route.params.site
      )
    }
  }
})
</script>
