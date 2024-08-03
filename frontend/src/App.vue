<template>
  <div class="app">
    <router-view :isChatOpen="isChatOpen" @toggleChat="toggleChat"></router-view>
  </div>
</template>

<script>
// import MainLayout from './components/MainLayout.vue'

export default {
  components: {
    // MainLayout
  }
}
</script>

<style>
.app {
  height: 100vh;
  margin: 0;
  padding: 0;
  font-family: 'Ubuntu', sans-serif;
}
.main-layout {
}

</style>
