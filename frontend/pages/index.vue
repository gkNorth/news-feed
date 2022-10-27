<template>
  <div>
    <section class="bg-white dark:bg-gray-900">
      <div class="container px-6 py-10 mx-auto">
        <h1 class="text-3xl font-semibold text-gray-800 capitalize lg:text-4xl dark:text-white">From the blog</h1>

        <div class="grid grid-cols-2 gap-8 mt-8 md:mt-16 md:grid-cols-3">

          <div
            v-for="feed in feeds"
            :key="feed.id"
          >
            <img
              class="object-cover w-full h-50 rounded-lg lg:w-64"
              :src="feed.page_img !== 'false' ? feed.page_img : require('~/assets/noimage.png')"
            >
            <div class="flex flex-col justify-between py-6 lg:mx-6">
              <span class="text-sm text-gray-500 dark:text-gray-300">{{feed.site_title}}</span>
              <a
                :href="feed.page_link"
                class="text-xl font-semibold text-gray-800 hover:underline dark:text-white"
                target='_blank'
                rel='noreferrer nofollow noopener'
              >
                  {{feed.page_title}}
              </a>
              <span class="text-sm text-gray-500 dark:text-gray-300 text-right">{{feed.created_at}}</span>
            </div>
          </div>

        </div>
      </div>
    </section>
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
