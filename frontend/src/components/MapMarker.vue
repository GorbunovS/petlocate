<template>
    <div class="map-marker">
      <div class="marker-icon">
        <CustomIcon :type="iconType" fillColor="white" />
      </div>
    </div>
  </template>
  
  <script>
  import CustomIcon from './CustomIcon.vue';
  
  export default {
    name: 'MapMarker',
    components: {
      CustomIcon
    },
    props: {
      type: {
        type: String,
        required: true
      },
      status: {
        type: String,
        required: true
      },
      position: {
        type: Object,
        required: true
      }
    },
    computed: {
      iconType() {
        // Возвращаем тип иконки, соответствующий типу пропса
        return this.type;
      },
      borderColor() {
        // Устанавливаем цвет обводки в зависимости от статуса
        switch (this.status) {
          case 'active':
            return 'green';
          case 'inactive':
            return 'gray';
          case 'pending':
            return 'yellow';
          default:
            return 'black';
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .map-marker {
    position: relative;
  }
  
  .marker-icon {
    width: 24px;
    height: 24px;
    display: flex;
    justify-content: center;
    align-items: center;
    border: 2px solid;
    border-color: var(--border-color); /* Устанавливается динамически через JavaScript */
    border-radius: 50%;
    background: white;
  }
  </style>
  