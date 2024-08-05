<template>
  <div class="map-container">
    <div id="map" class="map"></div>
    <div class="side-container">
      <div class="list-view">
        <ItemList 
          :items="items" 
          :selected-filter="selectedFilter" 
          :selected-item-id="selectedItemId"
          @item-selected="selectMarker" 
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
  data() {
    return {
      map: null,
      zoom: 12, // Значение увеличения по умолчанию
      center: [37.618423, 55.751244], // [lng, lat] - координаты центра Москвы
      selectedFilter: {
        type: null,
        time: null
      },
      selectedItemId: null,
      items: [] // Изначально пусто, данные будут загружены из API
    };
  },
  methods: {
    setupMap() {
      this.map = new maplibregl.Map({
        container: 'map',
        style: 'https://api.maptiler.com/maps/basic-v2/style.json?key=g7cM1vMR1viO2I3YInIA',
        center: this.center,
        zoom: this.zoom
      });

      this.map.on('load', () => {
        console.log('Map loaded');
        this.addCustomMarker(); // Добавляем маркер с кастомной иконкой
      });
    },

    addCustomMarker() {
      console.log('Adding a custom marker at center of Moscow');

      // Удаление предыдущих маркеров, если есть
      if (this.map.getLayer('custom-marker-layer')) {
        this.map.removeLayer('custom-marker-layer');
      }
      if (this.map.getSource('custom-marker-source')) {
        this.map.removeSource('custom-marker-source');
      }

      // Определение SVG иконки
      const svgIcon = `
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 19 19" width="40" height="40">
          <circle cx="9.5" cy="9.5" r="8" fill="white" stroke="#FF8A00" stroke-width="3"/>
        </svg>
      `;

      // Создание изображения из SVG
      const image = new Image();
      image.src = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svgIcon);

      // Добавление изображения в карту
      image.onload = () => {
        this.map.addImage('custom-icon', image);

        // Добавление источника данных
        this.map.addSource('custom-marker-source', {
          type: 'geojson',
          data: {
            type: 'FeatureCollection',
            features: [{
              type: 'Feature',
              properties: { id: 'moscow-center' },
              geometry: {
                type: 'Point',
                coordinates: this.center // Долгота, Широта
              }
            }]
          }
        });

        // Добавление слоя с кастомной иконкой
        this.map.addLayer({
          id: 'custom-marker-layer',
          type: 'symbol',
          source: 'custom-marker-source',
          layout: {
            'icon-image': 'custom-icon', // Используем кастомную SVG иконку
            'icon-size': 1 // Размер иконки
          }
        });

        // Опционально: Добавление слушателя клика для маркера
        this.map.on('click', 'custom-marker-layer', (e) => {
          console.log('Marker clicked', e.features[0].properties.id);
          this.map.flyTo({
            center: this.center,
            zoom: this.zoom
          });
        });
      };
    },

    updateFilter(newFilter) {
      this.selectedFilter = newFilter;
      // В этом случае обновление фильтра не требуется, так как у нас только один маркер
    }
  },
  mounted() {
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
