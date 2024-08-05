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
    items: [] // Изначально пустой массив
  },
  mutations: {
    setActiveChat(state, participantId) {
      state.activeChat = participantId;
    },
    addMessage(state, { participantId, message }) {
      state.messages[participantId].push(message);
    },
    setItems(state, items) {
      state.items = items;
    }
  },
  actions: {
    async fetchItems({ commit }) {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/items'); // Убедитесь, что URL совпадает с вашим Flask эндпоинтом
        commit('setItems', response.data);
      } catch (error) {
        console.error('Error fetching items:', error);
      }
    }
  },
  getters: {
    items: state => state.items
  }
});
