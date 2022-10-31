<template>
  <div>
    <ul class="flex overflow-auto">
      <li
        class="shrink-0 px-4 py-3"
        :class="[$route.params.site === undefined ? activeSiteClass : '']"
      >
        <nuxt-link to="/">HOME</nuxt-link>
      </li>
      <li
        v-for="(site, i) in sites"
        :key="i"
        class="shrink-0 px-4 py-3"
        :class="[site === $route.params.site ? activeSiteClass : '']"
      >
        <nuxt-link :to='`/${site}/`'>{{site}}</nuxt-link>
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  name: 'SiteSlide',
  props: {
    sites: {
      type: Array,
      required: false
    }
  },
  data() {
    return {
      activeSiteClass: 'border-b-2 border-cyan-900 text-cyan-900'
    }
  }
})
</script>
