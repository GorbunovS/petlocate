
<template>
    <div class="participant-list">
      <ul>
        <li
          v-for="participant in participants"
          :key="participant.id"
          :class="{ active: participant.id === activeChat }"
          @click="setActiveChat(participant.id)"
        >
          {{ participant.name }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import { mapState, mapMutations } from 'vuex';
  
  export default {
    computed: {
      ...mapState(['participants', 'activeChat'])
    },
    methods: {
      ...mapMutations(['setActiveChat'])
    }
  };
  </script>
  
  <style scoped>
  .participant-list {
    width: 200px;
    border-right: 1px solid #ccc;
  }
  
  .participant-list ul {
    list-style-type: none;
    padding: 0;
  }
  
  .participant-list li {
    padding: 10px;
    cursor: pointer;
  }
  
  .participant-list li.active {
    background-color: #ddd;
  }
  </style>
  