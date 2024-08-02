<template>
  <div class="map-container">
    <l-map :zoom="zoom" :center="center" style="height: 100vh; width: 100vw;">
      <l-tile-layer :url="url" :attribution="attribution" />
      <l-marker v-for="marker in markers" :key="marker.id" :lat-lng="marker.position" />
    </l-map>
    <div class="side-container">
      <div class="list-view">
        <ItemList :items="items" @item-selected="updateMarker" />
      </div>
      <!-- Conditionally render the chat container -->
      <div v-if="isChatOpen" class="chat-container">
        <ParticipantList />
        <ChatItem />
      </div>
    </div>
  </div>
</template>

<script>
import { LMap, LTileLayer, LMarker } from 'vue3-leaflet';
import 'leaflet/dist/leaflet.css';
import ParticipantList from './ParticipantList.vue';
import ChatItem from './ChatItem.vue';
import ItemList from './ItemList.vue';

export default {
  name: 'MapLayout',
  components: {
    LMap,
    LTileLayer,
    LMarker,
    ParticipantList,
    ChatItem,
    ItemList
  },
  props: {
    isChatOpen: {
      type: Boolean,
      required: true
    }
  },
  data() {
    return {
      zoom: 13,
      center: [55.751244, 37.618423], // Координаты центра карты
      url: 'https://tile.udev.su/styles/basemap/512/{z}/{x}/{y}.png',
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
      markers: [], // Массив маркеров
      items: [
        {
          id: 1,
          photo: 'https://via.placeholder.com/100',
          status: 'Утерян',
          type: 'dog',
          time: 'Около часа назад',
          location: 'г. Реутов Улица Октября',
          comment: 'Отзывается на кличку Тесла. Любит есть какашки',
          position: [55.760, 37.620] // Координаты для маркера
        },
        {
          id: 2,
          photo: 'https://via.placeholder.com/100',
          status: 'Найден',
          type: 'dog',
          time: 'Только что',
          location: 'г. Реутов Улица Октября',
          comment: 'Найден пёс около торгового центра Экватор. Похоже домашний',
          position: [55.765, 37.625] // Координаты для маркера
        }
        // Добавьте больше элементов по необходимости
      ]
    };
  },
  methods: {
    updateMarker(item) {
      this.markers = [{ id: item.id, position: item.position }];
      this.center = item.position;
    }
  }
};
</script>

<style scoped>
.map-container {
  position: relative;
  width: 100%;
  height: 100vh;
}

.side-container {
  display: flex;
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  align-items: flex-start; /* Align items to the top */
}

.list-view {
  width: auto;
  margin-top: 5px;
  height: 90vh;
  border-radius: 8px;
  overflow: hidden;
  z-index: 900; /* Ensures the list is on top of the map */
  margin-left: 5px; /* 5px margin from the list */
  background-color: rgb(234, 234, 234); /* Semi-transparent background */
}

/* Chat container */
.chat-container {
  width: 500px;
  height: 25vh;
  border-radius: 8px;
  overflow: hidden;
  margin-top: 5px;
  z-index: 900; /* Ensures the chat is on top of the map */
  background-color: rgba(255, 255, 255); /* Semi-transparent background */
  margin-left: 5px; /* 5px margin from the list */
}
</style>
