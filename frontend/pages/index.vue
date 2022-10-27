<template>
  <div>
    <ul>
      <li
        v-for="feed in feeds"
        :key="feed.id"
      >{{feed.page_title}}</li>
    </ul>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import { mapGetters } from 'vuex'

interface AsyncData {
  feeds: any
}

export default Vue.extend({
  name: 'IndexPage',
  async asyncData({ store }): Promise<void> {
    await store.dispatch('fetchFeeds')
  },
  computed: {
    ...mapGetters(['feeds'])
  }
})
</script>
