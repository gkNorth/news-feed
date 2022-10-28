<template>
  <header>
    <div class="flex justify-center align-middle p-4 bg-cyan-900">
      <nuxt-link
        to="/"
        class="text-white text-lg"
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
