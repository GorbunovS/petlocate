<template>
  <div class="map-with-form">
    <div id="map-container">
      <l-map
        style="width: 100%; height: 100%;"
        :zoom="zoom"
        :center="mapCenter"
        @update:zoom="zoomUpdated"
        @click="handleMapClick"
        :attributionControl="false"
      >
        <l-tile-layer
          :url="tileUrl"
          :attribution="tileAttribution"
        />
        <l-marker
          v-for="(marker, index) in markers"
          :key="index"
          :lat-lng="[marker.lat, marker.lon]"
        >
          <l-popup>
            <p>Радиус: {{ marker.radius }} метров</p>
            <p>Статус: {{ marker.status }}</p>
          </l-popup>
        </l-marker>
        <l-circle
          v-for="(marker, index) in markers"
          :key="index"
          :lat-lng="[marker.lat, marker.lon]"
          :radius="marker.radius"
          :color="marker.userId === userId ? userColor : '#f03'"
          :fill-opacity="circleStyle.fillOpacity"
        />
      </l-map>
    </div>
  </div>
</template>

<script>
import { LMap, LTileLayer, LMarker, LPopup, LCircle } from '@vue-leaflet/vue-leaflet';
import "leaflet/dist/leaflet.css";
import io from 'socket.io-client';

export default {
  components: {
    LMap, LTileLayer, LMarker, LPopup, LCircle
  },
  data() {
    return {
      location: '',
      file: null,
      time: '1', // Время по умолчанию (час)
      zoom: 10, // Начальный уровень масштабирования
      mapCenter: [55.751244, 37.618423], // Координаты центра (Москва)
      tileUrl: 'https://tile.udev.su/styles/basemap/512/{z}/{x}/{y}.png', // URL плиток карты
      tileAttribution: '© OpenStreetMap contributors', // Атрибуция карт
      markers: [],
      circleStyle: {
        fillColor: '#f03',
        fillOpacity: 0.5
      },
      socket: null,
      userId: '', // Идентификатор пользователя
      userColor: '#00f', // Цвет радиуса для текущего пользователя
    };
  },
  mounted() {
    this.userId = prompt('Введите ваш идентификатор (например, user1 или user2)');
    this.socket = io('http://localhost:3000', {
  transports: ['websocket'] // Попробуйте также ['polling', 'websocket']
} ); // Подключение к серверу WebSocket
    

    // Получение существующих маркеров
    this.socket.on('initMarkers', markers => {
      this.markers = markers;
    });

    // Обработка создания нового маркера
    this.socket.on('markerCreated', marker => {
      this.markers.push(marker);
    });
  },
  methods: {
  handleAddressSelected(address) {
    this.location = `${address.lon}, ${address.lat}`;
  },
  onFileChange(event) {
    this.file = event.target.files[0];
  },
  addPoint() {
    if (!this.location) {
      alert('Пожалуйста, выберите адрес.');
      return;
    }

    const [lon, lat] = this.location.split(',').map(Number);
    const initialRadius = this.getInitialRadius(this.time);

    if (isNaN(lat) || isNaN(lon)) {
      alert('Некорректные координаты.');
      return;
    }

    const marker = {
      lat,
      lon,
      radius: initialRadius,
      userId: this.userId, // Добавляем идентификатор пользователя
      status: 'нашел', // По умолчанию
    };

    // Отправка нового маркера на сервер
    this.socket.emit('createMarker', marker);

    // Обработка ошибки, если пользователь уже установил точку
    this.socket.on('error', (message) => {
      alert(message);
    });
  },
  getInitialRadius(hours) {
    switch (hours) {
      case '1': return 1000; // 1 км
      case '2': return 2000; // 2 км
      case '5': return 5000; // 5 км
      default: return 1000;
    }
  },
  handleMapClick(e) {
    const { latlng } = e;
    const marker = {
      lat: latlng.lat,
      lon: latlng.lng,
      radius: 1000, // 1 км
      userId: this.userId, // Добавляем идентификатор пользователя
      status: 'нашел', // По умолчанию
    };

    // Отправка нового маркера на сервер
    this.socket.emit('createMarker', marker);

    // Обработка ошибки, если пользователь уже установил точку
    this.socket.on('error', (message) => {
      alert(message);
    });
  },
  generateRandomLocation() {
    const minLat = 55.312; // Минимальная широта Московской области
    const maxLat = 56.009; // Максимальная широта Московской области
    const minLon = 36.803; // Минимальная долгота Московской области
    const maxLon = 38.903; // Максимальная долгота Московской области

    const lat = (Math.random() * (maxLat - minLat) + minLat).toFixed(6);
    const lon = (Math.random() * (maxLon - minLon) + minLon).toFixed(6);

    this.location = `${lon}, ${lat}`;
    this.mapCenter = [parseFloat(lat), parseFloat(lon)]; // Обновляем центр карты
  }
}

};
</script>

<style scoped>
/* Добавьте стиль для разного цвета радиусов и статусов */
.leaflet-control-attribution {
  display: none !important;
}

.map-with-form {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.add-point-form {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px;
  background-color: #f5f5f5;
  border-radius: 15px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.input-field {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
  outline: none;
  width: 150px;
}

.upload-button {
  display: inline-block;
  padding: 10px 15px;
  border-radius: 5px;
  background-color: #e0f0ff;
  color: #000;
  font-size: 16px;
  cursor: pointer;
  border: 1px solid #ccc;
  text-align: center;
}

.submit-button {
  padding: 10px 20px;
  border-radius: 5px;
  background-color: #a6e1a6;
  color: #000;
  font-size: 16px;
  cursor: pointer;
  border: none;
}

.submit-button:hover {
  background-color: #8fc88f;
}

.random-button {
  padding: 10px 15px;
  border-radius: 5px;
  background-color: #ffeb3b;
  color: #000;
  font-size: 16px;
  cursor: pointer;
  border: 1px solid #ccc;
}

.random-button:hover {
  background-color: #fdd835;
}

#map-container {
  flex-grow: 1;
  position: relative;
  width: 100%;
}

#map {
  width: 100%;
  height: 100%;
}
</style>
