<template>
  <div class="item-card" :class="{ selected: isSelected }" @click="selectItem">
    <div class="pic-container">
      <span class="item-status" :class="[statusClass, { 'selected-status': isSelected }]">{{ item.status }}</span>
      <img :src="item.photo" alt="Animal Photo" class="item-photo" />
    </div>
    <div class="item-info">
      <div class="info-container" :class="{ 'selected-info-container': isSelected }">
        <div class="info-header" :class="{ 'selected-header': isSelected }">Информация</div>
        <div class="info-content">
          <div class="item-time" :class="{ 'selected-time': isSelected }">
            <CustomIcon v-if="isRecentTime(item.time)" type="force" class="time-icon" />
            <span class="time-text">{{ item.time }}</span>
            <CustomIcon :type="item.type" class="item-icon" />
          </div>
        </div>
        <div class="item-location" :class="{ 'selected-location': isSelected }">{{ item.location }}</div>
      </div>
    </div>
    <div class="comment-container" :style="{ flexDirection: 'column', gap: '7px' }">
      <div class="info-header" :class="{ 'selected-header': isSelected }">Комментарий</div>
      <div class="item-comment" :class="{ 'selected-comment': isSelected }">{{ item.comment }}</div>
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

.item-location {
  color: #848484;
text-align: left;
font-size: 13px;
font-style: normal;
font-weight: 400;
line-height: normal;}
.pic-container {
  position: relative;
  width: 62px;
height: 62px;
flex-shrink: 0;

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
  font-size: 13px;
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
.item-card.selected .time-text {
  color: #ffffff; /* Новый цвет для .time-text при selected */
}
.item-card.selected .item-location {
  color: #eaeaea; /* Новый цвет для .item-location при selected */
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
width: 195px;
flex-direction: column;
justify-content: center;
align-items: flex-start;
gap: 7px;
flex-shrink: 0;}

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
  color: #BAB3B3;
font-family: Ubuntu;
font-size: 10px;
font-style: normal;
font-weight: 400;
line-height: normal;
}

.info-content {
  display: flex;
  flex-direction: column;
}

.item-time {
  display: flex;
  align-items: center;
  gap: 10px;

}

.time-icon {
  width: 13px;
  height: 16px;
}

.time-text {
  color: #000;
text-align: center;
font-family: Ubuntu;
font-size: 13px;
font-style: normal;
font-weight: 500;
line-height: normal;
}

.item-type, .item-comment {
  display: flex;
  width: 183px;
  padding: 10px;
  align-items: flex-start;
  gap: 10px;
  border-radius: 20px 20px 20px 0px;
  background: #E6E6E6;
  color: #6A6A6A;
  font-family: Ubuntu;
  font-size: 10px;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
}

.item-icon {
  width: 24px;
  height: 24px;
  margin-right: 5px;
}
</style>
