<template>
  <div class="grid grid-cols-2 gap-y-2 gap-x-5 mt-3 md:mt-16 md:grid-cols-3 px-6">
    <Card
      v-for="feed in feeds"
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
  computed: {
    ...mapGetters(['feeds']),
  }
})
</script>
