<template>
    <div class="main-page">
      <!-- Основной контент -->
      <div v-if="activeSection === 'map'">Map Content</div>
      <div v-if="activeSection === 'board'">Bulletin Board Content</div>
      <div v-if="activeSection === 'tips'">Tips Content</div>
      <div v-if="activeSection === 'contacts'">Contacts Content</div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'MainPage',
    data() {
      return {
        activeSection: 'map' // Начальная секция
      }
    },
    methods: {
      // Методы для управления контентом, если необходимо
    }
  }
  </script>
  
  <style scoped>
  .main-page {
    width: 900px;
    height: 900px;
    margin: 0 auto;
  }
  </style>
  