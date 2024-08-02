<!-- components/Chat.vue -->
<template>
    <div class="chat">
      <div class="messages" v-scrollable>
        <div v-for="(message, index) in currentMessages" :key="index" class="message">
          {{ message }}
        </div>
      </div>
      <div class="input">
        <input v-model="newMessage" @keyup.enter="sendMessage" placeholder="Type a message..." />
        <button @click="sendMessage">Send</button>
      </div>
    </div>
  </template>
  
  <script>
  import { mapState, mapMutations } from 'vuex';
  import { RecycleScroller } from 'vue-virtual-scroller'


  
  export default {
    directives: {
      RecycleScroller
    },
    data() {
      return {
        newMessage: ''
      };
    },
    computed: {
      ...mapState(['activeChat', 'messages']),
      currentMessages() {
        return this.messages[this.activeChat] || [];
      }
    },
    methods: {
      ...mapMutations(['addMessage']),
      sendMessage() {
        if (this.newMessage.trim()) {
          this.addMessage({ participantId: this.activeChat, message: this.newMessage.trim() });
          this.newMessage = '';
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .chat {
    flex: 1;
    display: flex;
    flex-direction: column;
  }
  
  .messages {
    flex: 1;
    overflow-y: auto;
    padding: 10px;
    border-bottom: 1px solid #ccc;
  }
  
  .message {
    margin-bottom: 10px;
  }
  
  .input {
    display: flex;
  }
  
  .input input {
    flex: 1;
    padding: 10px;
    border: 1px solid #ccc;
    border-right: none;
  }
  
  .input button {
    padding: 10px;
    border: 1px solid #ccc;
    background-color: #007bff;
    color: white;
    cursor: pointer;
  }
  
  .input button:hover {
    background-color: #0056b3;
  }
  </style>
  