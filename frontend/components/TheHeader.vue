<template>
  <header>
    <div class="flex justify-center align-middle py-3 bg-cyan-900">
      <nuxt-link
        to="/"
        class="text-white text-lg font-bold"
      >
        News Feed
      </nuxt-link>
    </div>
  </header>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  name: 'TheHeader',
})
</script>
