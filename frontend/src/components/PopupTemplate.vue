<template>
  <div class="popup-card">
    <div class="popup-photo-container">
      <img :src="item.photo" alt="Animal Photo" class="popup-photo" />
    </div>
    <div class="popup-info">
      <div class="popup-info-header">Информация</div>
      <div class="popup-info-content">
        <div class="popup-item-time">
          <span class="popup-time-text">{{ item.time }}</span>
          <span class="popup-item-icon">{{ item.type }}</span>
        </div>
        <div class="popup-item-location">{{ item.location }}</div>
      </div>
      <div class="popup-comment-container">
        <div class="popup-comment-header">Комментарий</div>
        <div class="popup-item-comment">{{ item.comment }}</div>
      </div>
    </div>
    <button class="popup-contact-button" @click="contact">Связаться</button>
  </div>
</template>

<script>
export default {
  props: {
    item: {
      type: Object,
      required: true
    }
  },
  methods: {
    contact() {
      // Логика для кнопки "Связаться"
      alert('Связаться');
    }
  }
};
</script>

<style scoped>
/* Стили для попапа */
.popup-card {
  display: flex;
  flex-direction: column;
  width: 300px;
  height: 400px;
  border-radius: 8px;
  overflow: hidden;
  background: #fff;
  font-family: Ubuntu, sans-serif;
}

.popup-photo-container {
  width: 100%;
  height: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.popup-photo {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.popup-info {
  padding: 10px;
  display: flex;
  flex-direction: column;
  height: 50%;
  box-sizing: border-box;
}

.popup-info-header {
  font-size: 14px;
  font-weight: bold;
  color: #333;
  margin-bottom: 5px;
}

.popup-info-content {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.popup-item-time {
  display: flex;
  align-items: center;
  gap: 10px;
}

.popup-time-text {
  font-size: 12px;
  color: #000;
}

.popup-item-icon {
  width: 24px;
  height: 24px;
}

.popup-item-location {
  font-size: 13px;
  color: #848484;
}

.popup-comment-container {
  margin-top: 10px;
}

.popup-comment-header {
  font-size: 14px;
  font-weight: bold;
  color: #333;
}

.popup-item-comment {
  font-size: 12px;
  color: #6A6A6A;
}

.popup-contact-button {
  margin-top: auto;
  background: #007bff;
  color: white;
  border: none;
  padding: 10px;
  cursor: pointer;
  border-radius: 0 0 8px 8px;
  font-size: 14px;
  font-weight: bold;
  text-align: center;
}

.popup-contact-button:hover {
  background: #0056b3;
}
</style>
