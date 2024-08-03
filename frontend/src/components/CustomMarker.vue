<template>
    <l-marker :lat-lng="latLng" :icon="icon" />
  </template>
  
  <script>
  import { LMarker } from 'vue3-leaflet';
  import L from 'leaflet';
  
  export default {
    name: 'CustomMarker',
    components: {
      LMarker
    },
    props: {
      latLng: {
        type: Array,
        required: true
      }
    },
    data() {
      return {
        icon: L.divIcon({
          className: 'custom-icon',
          html: `
            <div style="
              width: 30px;
              height: 30px;
              background-color: blue;
              border-radius: 50%;
              border: 2px solid white;
              display: flex;
              align-items: center;
              justify-content: center;
              font-size: 16px;
              color: white;
              text-align: center;
              line-height: 30px;
            ">
              F
            </div>
          `,
          iconSize: [30, 30]
        })
      };
    }
  };
  </script>
  
  <style scoped>
  .custom-icon {
    background: transparent;
  }
  </style>
  