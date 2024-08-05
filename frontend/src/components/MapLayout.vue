<template>
  <div class="map-container">
    <div id="map" class="map"></div>
    <div class="side-container">
      <div class="list-view">
        <ItemList 
          :items="items" 
          :selected-filter="selectedFilter" 
          :selected-item-id="selectedItemId"
          @item-selected="handleItemSelected"
          @filter-changed="updateFilter"
        />
      </div>
      <transition name="chat-container" @before-enter="beforeEnter" @enter="enter" @leave="leave">
        <div v-if="isChatOpen" class="chat-container">
          <ParticipantList />
          <ChatItem />
        </div>
      </transition>
    </div>
    <DebugInfo :selectedItemId="selectedItemId" />
  </div>
</template>

<script>
import { createApp } from 'vue';
import PopupItem from './PopupItem.vue';
import { mapGetters } from 'vuex';
import maplibregl from 'maplibre-gl';
import 'maplibre-gl/dist/maplibre-gl.css';
import ItemList from './ItemList.vue';
import ParticipantList from './ParticipantList.vue';
import ChatItem from './ChatItem.vue';
import DebugInfo from './DebugInfo.vue';

export default {
  name: 'MapLayout',
  components: {
    ItemList,
    ParticipantList,
    ChatItem,
    DebugInfo
  },
  props: {
    isChatOpen: {
      type: Boolean,
      required: true
    }
  },
  computed: {
    ...mapGetters(['items'])
  },
  data() {
    return {
      map: null,
      zoom: 12,
      center: [37.618423, 55.751244],
      selectedFilter: {
        type: null,
        time: null
      },
      selectedItemId: null,
      popup: null
    };
  },
  methods: {
    async setupMap() {
      this.map = new maplibregl.Map({
        container: 'map',
        style: 'https://api.maptiler.com/maps/basic-v2/style.json?key=g7cM1vMR1viO2I3YInIA',
        center: this.center,
        zoom: this.zoom
      });

      this.map.on('load', () => {
        this.addMarkers();
        this.updateMarkers();

        this.map.on('click', 'custom-marker-layer', (event) => {
          const feature = event.features[0];
          const coordinates = feature.geometry.coordinates.slice();
          const itemId = feature.properties.id;
          this.openPopup(itemId, coordinates);
        });

        this.map.on('mouseenter', 'custom-marker-layer', () => {
          this.map.getCanvas().style.cursor = 'pointer';
        });

        this.map.on('mouseleave', 'custom-marker-layer', () => {
          this.map.getCanvas().style.cursor = '';
        });
      });
    },

    addMarkers() {
      const statusColors = {
        lost: '#FF8A00',
        found: '#00A3FF'
      };

      const getIconSvg = (color) => `
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 19 19" width="40" height="40">
          <circle cx="9.5" cy="9.5" r="8" fill="white" stroke="${color}" stroke-width="3"/>
        </svg>`;

      Object.keys(statusColors).forEach(status => {
        const svgIcon = getIconSvg(statusColors[status]);
        const image = new Image();
        image.src = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svgIcon);

        image.onload = () => {
          if (!this.map.getImage(`icon-${status}`)) {
            this.map.addImage(`icon-${status}`, image);
          }
        };
      });

      const features = this.items.map(item => ({
        type: 'Feature',
        properties: { id: item.id, type: item.type, status: item.status },
        geometry: {
          type: 'Point',
          coordinates: item.position
        }
      }));

      this.map.addSource('custom-marker-source', {
        type: 'geojson',
        data: {
          type: 'FeatureCollection',
          features: features
        }
      });

      this.map.addLayer({
        id: 'custom-marker-layer',
        type: 'symbol',
        source: 'custom-marker-source',
        layout: {
          'icon-image': ['case',
            ['==', ['get', 'status'], 'Утерян'], 'icon-lost',
            ['==', ['get', 'status'], 'Найден'], 'icon-found',
            'default-icon'
          ],
          'icon-size': 1
        }
      });
    },

    updateMarkers() {
      if (!this.map) {
        console.error('Map is not initialized');
        return;
      }

      const filterType = this.selectedFilter.type;
      const filterExpression = filterType ? ['==', ['get', 'type'], filterType] : ['!=', ['get', 'type'], 'null'];

      this.map.setFilter('custom-marker-layer', filterExpression);
    },

    updateFilter(newFilter) {
      this.selectedFilter = newFilter;
      this.updateMarkers();
    },

    handleItemSelected(item) {
      this.selectedItemId = item.id;
      const coordinates = item.position;
      this.map.flyTo({
        center: coordinates,
        zoom: this.zoom
      });
      this.openPopup(item.id, coordinates);
    },

    openPopup(itemId, coordinates) {
      const item = this.items.find(i => i.id === itemId);
      if (item) {
        if (this.popup) {
          this.popup.remove();
        }

        this.popup = new maplibregl.Popup({ closeButton: false })
          .setLngLat(coordinates)
          .setDOMContent(this.createPopupContent(item))
          .addTo(this.map);
      }
    },

    createPopupContent(item) {
      const container = document.createElement('div');
      const app = createApp(PopupItem, { item });
      const popupElement = document.createElement('div');
      app.mount(popupElement);
      container.appendChild(popupElement);
      return container;
    }
  },
  async mounted() {
    await this.$store.dispatch('fetchItems');
    this.setupMap();
  }
};
</script>

<style scoped>
.map {
  width: 100%;
  height: 100%;
}

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

.custom-overlay {
  background-color: rgba(0,0,0,0.5);
  color: white;
  padding: 10px;
  border-radius: 5px;
  font-size: 12px;
  text-align: center;
}
</style>
