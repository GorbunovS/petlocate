import { createStore } from 'vuex';
import axios from 'axios';

export default createStore({
  state: {
    participants: [
      { id: 1, name: 'Alice' },
      { id: 2, name: 'Bob' }
    ],
    messages: {
      1: [],
      2: []
    },
    activeChat: 1,
    items: [ {
      id: 1,
      photo: 'https://via.placeholder.com/100',
      status: 'Утерян',
      type: 'cat',
      time: 'Около часа назад',
      location: 'г. Реутов Улица Октября',
      comment: 'Отзывается на кличку Тесла. Любит есть какашки',
      position: [55.760, 37.620] // Координаты для маркера
    }] // Добавляем состояние для items
  },
  mutations: {
    setActiveChat(state, participantId) {
      state.activeChat = participantId;
    },
    addMessage(state, { participantId, message }) {
      state.messages[participantId].push(message);
    },
    setItems(state, items) {
      state.items = items; // Мутация для обновления items
    }
  },
  actions: {
    async fetchItems({ commit }) {
      try {
        const response = await axios.get('https://api.example.com/items'); // Ваш URL API
        commit('setItems', response.data);
      } catch (error) {
        console.error('Error fetching items:', error);
      }
    }
  },
  getters: {
    items: state => state.items // Геттер для получения items
  }
});
