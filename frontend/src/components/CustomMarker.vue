<template>
  <div>
    <l-image-overlay
      :bounds="markerBounds"
      :url="imageUrl"
      @click="openPopup"
    />
    <l-popup v-if="showPopup" :lat-lng="latLng" @close="closePopup">
      <PopupTemplate :item="item" />
    </l-popup>
  </div>
</template>

<script>
import { LImageOverlay, LPopup } from 'vue3-leaflet';
import PopupTemplate from './PopupItem.vue';

export default {
  name: 'CustomMarker',
  components: {
    LImageOverlay,
    LPopup,
    PopupTemplate
  },
  props: {
    item: {
      type: Object,
      required: true
    },
    latLng: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      showPopup: false
    };
  },
  computed: {
    imageUrl() {
      const color = this.item.status === 'Утерян' ? 'orange' : 'blue';
      return `data:image/svg+xml;base64,${btoa(`
        <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40">
          <circle cx="20" cy="20" r="15" stroke="${color}" stroke-width="4" fill="white" />
        </svg>
      `)}`;
    },
    markerBounds() {
      const [lat, lng] = this.latLng;
      const offset = 0.0001; // Adjust this value to make the circle bigger or smaller
      return [[lat - offset, lng - offset], [lat + offset, lng + offset]];
    }
  },
  methods: {
    openPopup() {
      this.showPopup = true;
    },
    closePopup() {
      this.showPopup = false;
    }
  },
  mounted() {
    console.log('CustomMarker mounted:', this.item);
  }
};
</script>

<style scoped>
/* Add any necessary styles here */
</style>
