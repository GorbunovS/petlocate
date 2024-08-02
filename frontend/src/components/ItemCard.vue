<template>
  <div class="item-card" :class="{ selected: isSelected }" @click="selectItem">
    <div class="pic-container">
      <span class="item-status" :class="statusClass">{{ item.status }}</span>
      <img :src="item.photo" alt="Animal Photo" class="item-photo" />
    </div>
    <div class="item-info">
      <div class="info-container">
        <div class="info-header">Информация</div>
        <div class="info-content">
          <div class="item-time">
            <CustomIcon v-if="isRecentTime(item.time)" type="force" class="time-icon" />
            <span class="time-text">{{ item.time }}</span>
            <CustomIcon :type="item.type" class="item-icon" />
          </div>
        </div>
        <div class="item-location">{{ item.location }}</div>
      </div>
    </div>
    <div class="item-comment">{{ item.comment }}</div>
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
    },
    isSelected: {
      type: Boolean,
      default: false
    }
  },
  computed: {
    statusClass() {
      return this.item.status === 'Утерян' ? 'lost' : 'found';
    }
  },
  methods: {
    selectItem() {
      this.$emit('select', this.item);
    },
    isRecentTime(time) {
      return time === 'Только что' || time === 'Около часа назад';
    }
  }
};
</script>

<style scoped>
.pic-container {
  position: relative;
  width: 100px;
  height: 100px;
}

.item-photo {
  min-width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 8px;
}

.item-status {
  position: absolute;
  width: 100%;
  bottom: 0;
  left: 0;
  font-weight: bold;
  padding: 2px 6px;
  border-radius: 4px;
  color: #FFF;
  text-align: center;
  box-sizing: border-box;
}

.item-card {
  display: flex;
  width: 510px;
  padding: 7px 10px;
  align-items: center;
  gap: 11px;
  background: #FFF;
  transition: background 0.1s;
  cursor: pointer;
  border-bottom: 1px solid #e6e6e6;
}

.item-card.selected {
  background: #9747FF;
  color: white;
}

.item-card.selected:hover {
  background: #9747FF;
  color: white;
}

.item-card:hover {
  background: #efefef;
}

.item-info {
  display: flex;
  flex-direction: column;
  justify-content: center;
  flex: 1;
}

.info-container {
  width: 195px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  border-radius: 8px;
  padding: 10px;
  text-align: left; /* Align text and inline elements to the left */
}

.info-header {
  color: #d0d0d0;
  padding: 5px;
  border-radius: 4px;
  font-weight: normal;
  text-align: center;
}

.info-content {
  display: flex;
  flex-direction: column;
}

.item-time {
  display: flex;
  align-items: center;
  font-size: 0.9em;
  color: #757575;
  margin-bottom: 5px;
}

.time-icon {
  width: 24px;
  height: 24px;
  margin-right: 5px;
}

.time-text {
  font-weight: bold;
}

.item-type, .item-comment {
  margin-bottom: 5px;
  display: flex;
  align-items: center;
  background: silver;
}

.item-icon {
  width: 24px;
  height: 24px;
  margin-right: 5px;
}
</style>
