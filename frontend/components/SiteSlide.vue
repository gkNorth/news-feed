<template>
  <div>
    <ul class="flex overflow-auto">
      <li
        v-for="(site, i) in sites"
        :key="site.i"
        class="mr-3 shrink-0"
      >
        <a :href='`/${site}/`'>{{site}}</a>
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
  }
})
</script>
