<template>
  <div class="map-container">
    <l-map :zoom="zoom" :center="center" style="height: 100vh; width: 100vw;">
      <l-tile-layer :url="url" :attribution="attribution" />
      <l-marker
        v-for="marker in markers"
        :key="marker.id"
        :lat-lng="marker.position"
      >
        <l-popup>
          <img :src="marker.photo" alt="Photo" style="width: 100px; height: auto;" />
          <div><strong>Status:</strong> {{ marker.status }}</div>
          <div><strong>Type:</strong> {{ marker.type }}</div>
          <div><strong>Time:</strong> {{ marker.time }}</div>
          <div><strong>Location:</strong> {{ marker.location }}</div>
          <div><strong>Comment:</strong> {{ marker.comment }}</div>
        </l-popup>
      </l-marker>
    </l-map>
    <div class="side-container">
      <div class="list-view">
        <ItemList :items="items" @item-selected="updateMarker" />
      </div>
      <transition name="chat-container" @before-enter="beforeEnter" @enter="enter" @leave="leave">
        <div v-if="isChatOpen" class="chat-container">
          <ParticipantList />
          <ChatItem />
        </div>
      </transition>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import { LMap, LTileLayer, LMarker, LPopup } from 'vue3-leaflet';
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
    LPopup,
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
      center: [55.751244, 37.618423],
      url: 'https://tile.udev.su/styles/basemap/512/{z}/{x}/{y}.png',
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
      markers: [] // Список маркеров будет заполнен данными
    };
  },
  computed: {
    ...mapState(['items'])
  },
  methods: {
    ...mapActions(['fetchItems']),
    updateMarker(item) {
      // Обновляем центр карты на позицию выбранного маркера
      this.center = [item.position.lat, item.position.lng];
    }
  },
  watch: {
    items(newItems) {
      // Обновляем маркеры при изменении items
      this.markers = newItems.map(item => ({
        id: item.id,
        position: { lat: item.position[0], lng: item.position[1] },
        photo: item.photo,
        status: item.status,
        type: item.type,
        time: item.time,
        location: item.location,
        comment: item.comment
      }));
      // Обновляем центр карты на среднюю позицию маркеров, если их много
      if (this.markers.length > 0) {
        const latSum = this.markers.reduce((sum, marker) => sum + marker.position.lat, 0);
        const lngSum = this.markers.reduce((sum, marker) => sum + marker.position.lng, 0);
        this.center = [latSum / this.markers.length, lngSum / this.markers.length];
      }
    }
  },
  created() {
    this.fetchItems(); // Получаем данные при создании компонента
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
  align-items: flex-start;
}

.list-view {
  width: auto;
  margin-top: 5px;
  height: 90vh;
  border-radius: 8px;
  overflow: hidden;
  z-index: 900;
  margin-left: 5px;
  background-color: rgb(234, 234, 234);
}

.chat-container {
  width: 500px;
  height: 25vh;
  border-radius: 8px;
  overflow: hidden;
  margin-top: 20px;
  z-index: 900;
  background-color: rgba(255, 255, 255);
  margin-left: 77vw;
  position: absolute;
  transition: opacity 0.3s ease, transform 0.3s ease;
}

.chat-container-enter-active,
.chat-container-leave-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}

.chat-container-enter, 
.chat-container-leave-to {
  opacity: 0;
  transform: translateX(100%);
}
</style>
