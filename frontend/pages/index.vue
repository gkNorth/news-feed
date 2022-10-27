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
import { Component, Vue, Watch } from 'nuxt-property-decorator'
import { Getter, Action } from 'vuex-class'
import { Context } from '@nuxt/vue-app'
import * as Vuex from 'vuex'

interface AsyncData {
  feeds: any
}
@Component({})
export default class IndexPage extends Vue {
  $store!: Vuex.ExStore

  @Getter('feeds') feeds!: any
  @Action('fetchFeeds') fetchFeeds: any

  async asyncData({}) {
    console.log(this.$store.fetchFeeds())
  }
}
</script>
