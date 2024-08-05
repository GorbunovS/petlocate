<template>
  <div class="container">
    <div class="subheader">
      Объявления
    </div>
    <div class="filters">
      <button 
        class="filter-button" 
        :class="{ active: selectedFilter.type === 'cat' }"
        @click="toggleFilter('type', 'cat')"
      >
        <CustomIcon fillColor="black" type="cat"/>
        Кошки
      </button>
      <button 
        class="filter-button" 
        :class="{ active: selectedFilter.type === 'dog' }"
        @click="toggleFilter('type', 'dog')"
      >
        <CustomIcon fillColor="black" type="dog"/>
        Собаки
      </button>
      <button 
        class="filter-button" 
        :class="{ active: selectedFilter.time === 'last_hour' }"
        @click="toggleFilter('time', 'last_hour')"
      >
        <CustomIcon fillColor="black" type="force"/>
        Последние
      </button>
      <button 
        class="reset-button"
        @click="resetFilters"
      >
        Reset Filters
      </button>
    </div>
    <div v-if="filteredItems.length === 0" class="no-items-message">
      Нет доступных элементов.
    </div>
    <div class="item-list">
      <ItemCard 
        v-for="item in filteredItems" 
        :key="item.id" 
        :item="item" 
        :isSelected="item.id === selectedItemId" 
        @select="selectItem"
      />
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import ItemCard from './ItemCard.vue';
import CustomIcon from './icons/CustomIcon.vue';

export default {
  components: {
    ItemCard,
    CustomIcon
  },
  data() {
    return {
      selectedFilter: {
        type: null,
        time: null
      },
      selectedItemId: null
    };
  },
  computed: {
    ...mapGetters(['items']),
    filteredItems() {
      return this.items.filter(item => {
        const typeFilter = this.selectedFilter.type ? item.type === this.selectedFilter.type : true;
        const timeFilter = this.selectedFilter.time ? this.isInTimeFilter(item.time) : true;
        return typeFilter && timeFilter;
      });
    }
  },
  methods: {
    selectItem(item) {
      this.selectedItemId = item.id;
      this.$emit('item-selected', item);
    },
    toggleFilter(filterType, value) {
      const newFilter = { ...this.selectedFilter };
      newFilter[filterType] = newFilter[filterType] === value ? null : value;
      this.selectedFilter = newFilter; // Обновление локального состояния фильтров
    },
    resetFilters() {
      this.selectedFilter = { type: null, time: null }; // Сброс фильтров
    },
    isInTimeFilter(itemTime) {
      const now = new Date();
      const itemTimeDate = new Date(itemTime); 
      const oneHourAgo = new Date(now.getTime() - (60 * 60 * 1000));
      return itemTimeDate > oneHourAgo;
    }
  },
  async mounted() {
    // Вызов действия для загрузки данных
    await this.$store.dispatch('fetchItems');
  }
};
</script>

<style scoped>
.container {
  width: 100%;
}

.subheader {
  text-align: center;
  padding: 6px 0;
  font-size: 13px;
  background: #ffffff;
}

.filters {
  display: flex;
  margin-top: 5px;
  justify-content: center;
  align-items: center;
  gap: 10px;
  padding: 10px 0;
  background: #ffffff;
  width: 100%;
}

.filter-button {
  display: flex;
  align-items: center;
  gap: 5px;
  background: none;
  border: none;
  padding: 5px 10px;
  cursor: pointer;
  font-size: 12px;
  color: #898989;
  background-color: rgb(238, 238, 238);
  border-radius: 20px;
  transition: background-color 0.3s;
}

.filter-button.active {
  background-color: #007bff;
  color: white;
}

.reset-button {
  background: none;
  border: none;
  padding: 5px 10px;
  cursor: pointer;
  font-size: 13px;
  color: #ff0000;
  transition: color 0.3s;
}

.reset-button:hover {
  color: #d10000;
}

.item-list {
  margin-top: 5px;
  height: calc(100vh - 120px); /* Adjust height as needed */
  overflow-y: auto;
  background: rgba(240, 240, 240, 0.8);
}

.no-items-message {
  text-align: center;
  padding: 20px;
  color: #999;
}
</style>
