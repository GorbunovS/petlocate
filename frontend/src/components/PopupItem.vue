<template>
  <div class="popup-item">
    <div class="popup-pic-container">
      <span class="popup-status" :class="statusClass">{{ item.status }}</span>
      <img :src="item.photo" alt="Animal Photo" class="popup-photo" />
    </div>
    <div class="popup-info">
      <div class="popup-info-header">Информация</div>
      <div class="popup-info-content">
        <div class="popup-time">
          <CustomIcon v-if="isRecentTime(item.time)" type="force" class="popup-time-icon" />
          <span class="popup-time-text">{{ item.time }}</span>
          <CustomIcon :type="item.type" class="popup-item-icon" />
        </div>
        <div class="popup-location">{{ item.location }}</div>
      </div>
      <div class="popup-comment">
        <div class="popup-comment-header">Комментарий</div>
        <div class="popup-comment-content">{{ item.comment }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import CustomIcon from '@/components/icons/CustomIcon.vue';

export default {
  components: {
    CustomIcon
  },
  props: {
    item: {
      type: Object,
      required: true
    }
  },
  computed: {
    statusClass() {
      return this.item.status === 'Утерян' ? 'lost' : 'found';
    }
  },
  methods: {
    isRecentTime(time) {
      return time === 'Только что' || time === 'Около часа назад';
    }
  }
};
</script>

<style scoped>
.popup-item {
  display: flex;
  flex-direction: column;
  max-width: 250px;
  background: #FFF;
  padding: 10px;
  border-radius: 8px;
}

.popup-pic-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 10px;
}

.popup-photo {
  width: 100%;
  height: auto;
  border-radius: 8px;
  object-fit: cover;
}

.popup-status {
  margin-top: 5px;
  font-size: 12px;
  font-weight: bold;
  color: #FFF;
  background-color: #000; /* Customize as needed */
  padding: 2px 6px;
  border-radius: 4px;
  text-align: center;
}

.popup-info {
  display: flex;
  flex-direction: column;
}

.popup-info-header {
  font-size: 12px;
  color: #BAB3B3;
  margin-bottom: 5px;
}

.popup-info-content {
  display: flex;
  flex-direction: column;
}

.popup-time {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 5px;
}

.popup-time-icon {
  width: 13px;
  height: 16px;
}

.popup-time-text {
  font-size: 13px;
  font-weight: 500;
}

.popup-location {
  font-size: 13px;
  color: #848484;
}

.popup-comment {
  margin-top: 10px;
}

.popup-comment-header {
  font-size: 12px;
  color: #BAB3B3;
  margin-bottom: 5px;
}

.popup-comment-content {
  font-size: 12px;
  color: #6A6A6A;
}
</style>
