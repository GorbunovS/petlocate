// store/index.js
import { createStore } from 'vuex';

export default createStore({
  state: {
    participants: [
      { id: 1, name: 'Alice' },
      { id: 2, name: 'Bob' },
    ],
    messages: {
      1: [],
      2: []
    },
    activeChat: 1
  },
  mutations: {
    setActiveChat(state, participantId) {
      state.activeChat = participantId;
    },
    addMessage(state, { participantId, message }) {
      state.messages[participantId].push(message);
    }
  }
});
