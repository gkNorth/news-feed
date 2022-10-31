<template>
  <div>
    <a
      :href="feed.page_link"
      target='_blank'
      rel='noreferrer nofollow noopener'
    >
      <img
        class="object-cover w-full h-50 rounded-lg lg:w-64 aspect-[4/3]"
        :src="feed.page_img !== 'false' ? feed.page_img : require('~/assets/noimage.png')"
      >
    </a>
    <div class="flex flex-col justify-between py-2 lg:mx-6">
      <span class="text-sm text-gray-500 dark:text-gray-300">{{feed.site_title}}</span>
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
import Vue from 'vue';

export default Vue.extend({
  name: 'Card',
  props: {
    feed: {
      type: Object,
      required: true
    }
  }
})
</script>
