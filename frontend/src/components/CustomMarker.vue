<!-- CustomMarker.vue -->
<template>
  <l-marker :lat-lng="latLng" :icon="customIcon">
    <slot></slot>
  </l-marker>
</template>

<script>
import { defineComponent } from 'vue';
import { LMarker } from 'vue3-leaflet';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';

export default defineComponent({
  name: 'CustomMarker',
  components: {
    LMarker,
  },
  props: {
    latLng: {
      type: Object,
      required: true,
    },
    iconUrl: {
      type: String,
      required: true,
    },
    iconSize: {
      type: Array,
      default: () => [25, 41],
    },
    iconAnchor: {
      type: Array,
      default: () => [12, 41],
    },
    popupAnchor: {
      type: Array,
      default: () => [1, -34],
    },
  },
  computed: {
    customIcon() {
      return L.icon({
        iconUrl: this.iconUrl,
        iconSize: this.iconSize,
        iconAnchor: this.iconAnchor,
        popupAnchor: this.popupAnchor,
      });
    },
  },
});
</script>

<style scoped>
</style>
