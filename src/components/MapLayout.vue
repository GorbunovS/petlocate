<template>
  <div class="map-container">
    <l-map :zoom="zoom" :center="center" style="height: 100vh;width:100%;">
      <l-tile-layer
        :url="url"
        :attribution="attribution"
      />
      <l-marker :lat-lng="markerPosition" />
    </l-map>
  </div>
</template>

<script>
import { LMap, LTileLayer, LMarker } from 'vue3-leaflet';
import 'leaflet/dist/leaflet.css';

export default {
  name: 'MapLayout',
  components: {
    LMap,
    LTileLayer,
    LMarker
  },
  data() {
    return {
      zoom: 13,
      center: [55.751244, 37.618423], // Координаты центра карты
      url: 'https://tile.udev.su/styles/basemap/512/{z}/{x}/{y}.png',
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
      markerPosition: [51.505, -0.09] // Координаты маркера
    }
  }
}
</script>

<style scoped>
.map-container {
  width: 100vh;
  height: 100%;
}
</style>
