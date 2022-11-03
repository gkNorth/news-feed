<template>
  <div v-if="filteredFeedsBySite.length">
    <div class="flex items-center justify-center gap-2">
      <span class="text-sm text-gray-500">The Numbers of Favorite :</span>
      <span class="text-sm text-gray-700">{{filteredFeedsBySite.length}}</span>
    </div>
    <div class="mt-3 md:mt-16 md:grid-cols-3 px-4">
      <Card
        v-for="feed in filteredFeedsBySite"
        :key="feed.id"
        :feed="feed"
      />
    </div>
  </div>
  <div v-else>
    <p class="text-center p-5">There are currently no favorites...</p>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import { Feed } from 'types'
import Card from '~/components/Card.vue'

export default Vue.extend({
  name: 'IndexPage',
  components: {
    Card,
  },
  computed: {
    filteredFeedsBySite(): Feed[] {
      return this.$store.getters.feeds.filter(
        (feed: Feed) => feed.favorite === true
      )
    }
  }
})
</script>
