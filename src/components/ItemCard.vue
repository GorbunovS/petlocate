<template>
    <div class="item-card" :class="{ selected: isSelected }" @click="selectItem">
      <div class="pic-container">
        <span class="item-status" :class="statusClass">{{ item.status }}</span>
      <img :src="item.photo" alt="Animal Photo" class="item-photo" />
      </div>
      <div class="item-info">
        <div class="item-header">
          <span class="item-time">{{ item.time }}</span>
        </div>
        <div class="item-type">
          <img :src="getTypeIcon(item.type)" alt="Animal Type" class="item-icon" />
          {{ item.type }}
        </div>
        <div class="item-location">{{ item.location }}</div>
        <div class="item-comment">{{ item.comment }}</div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
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
      getTypeIcon(type) {
        return type === 'dog' ? '/path/to/dog-icon.png' : '/path/to/cat-icon.png';
      },
      selectItem() {
        this.$emit('select', this.item);
      }
    }
  };
  </script>
  
  <style scoped>
.pic-container {
  position: relative; /* Ensures that item-status is positioned relative to this container */
  width: 100px; /* Set to match the size of item-photo */
  height: 100px; /* Set to match the size of item-photo */
}

.item-photo {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 8px;
}

.item-status {
  position: absolute; 
  width: 100%; /* Matches the width of the photo */
  bottom: 0; /* Aligns the bottom of the status with the bottom of the .pic-container */
  left: 0; /* Aligns the status with the left of the .pic-container */
  font-weight: bold;
  padding: 2px 6px;
  border-radius: 4px;
  color: #FFF;
  text-align: center; /* Centers the text within the status */
  box-sizing: border-box; /* Includes padding and border in the element’s total width and height */
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

.item-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 5px;
}



.item-status.lost {
  background-color: #FFA000;
}

.item-status.found {
  background-color: #00C853;
}

.item-time {
  font-size: 0.9em;
  color: #757575;
}

.item-type, .item-location, .item-comment {
  margin-bottom: 5px;
  display: flex;
  align-items: center;
}

.item-icon {
  width: 20px;
  height: 20px;
  margin-right: 5px;
}
</style>
