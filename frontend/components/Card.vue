<template>
  <div class="card bg-neutral-100 px-3 py-1 mb-2 rounded-md relative dark:bg-zinc-900">
    <span class="absolute top-1 right-2 text-sm">{{feed.emoji}}</span>
    <!-- <a
      :href="feed.page_link"
      target='_blank'
      rel='noreferrer nofollow noopener'
    >
      <img
        class="object-cover w-full h-50 rounded-lg lg:w-64 aspect-[4/3]"
        :src="feed.page_img !== 'false' ? feed.page_img : require('~/assets/noimage.png')"
      >
    </a> -->
    <div class="flex flex-col justify-between py-2 lg:mx-6">
      <div class="flex items-center gap-3">
        <span class="text-sm text-gray-500 dark:text-gray-300">{{feed.site_title}}</span>
        <span
          v-if="isNew"
          class="text-sm text-red-500 dark:text-orange-600"
        >
            New
        </span>
      </div>
      <a
        :href="feed.page_link"
        class="text-base break-words font-semibold text-gray-800 hover:underline dark:text-white"
        target='_blank'
        rel='noreferrer nofollow noopener'
      >
          {{feed.page_title}}
      </a>
      <span class="text-sm text-gray-500 dark:text-gray-300 text-right">{{feed.created_at}}</span>
    </div>
  </div>
</template>

<script lang="ts">
import Vue, { PropOptions } from 'vue';
import { Feed } from 'types'
import dayjs from 'dayjs';

export default Vue.extend({
  name: 'Card',
  props: {
    feed: {
      type: Object,
      required: true
    } as PropOptions<Feed>
  },
  computed: {
    isNew(): boolean {
      const created_at: string = this.feed.created_at
      const today: string = dayjs(new Date()).format("YYYY-MM-DD")
      return created_at === today
    }
  }
})
</script>
