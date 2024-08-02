<template>
    <div class="item-list">
      <ItemCard 
        v-for="item in items" 
        :key="item.id" 
        :item="item" 
        :isSelected="item.id === selectedItemId" 
        @select="selectItem"
      />
    </div>
  </template>
  
  <script>
  import ItemCard from './ItemCard.vue';
  
  export default {
    components: {
      ItemCard
    },
    props: {
      items: {
        type: Array,
        required: true
      }
    },
    data() {
      return {
        selectedItemId: null
      };
    },
    methods: {
      selectItem(item) {
        this.selectedItemId = item.id;
        this.$emit('item-selected', item);
      }
    }
  };
  </script>
  
  <style scoped>
  .item-list {
    height: 100vh;
    overflow-y: auto;
    background: rgba(240, 240, 240, 0.8);
  }
  </style>
  