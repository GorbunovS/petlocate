<template>
  <div class="main-layout">
    <header class="header">
      <div class="header-left">
        <img class="logo" src="@/assets/text-logo.svg" alt="Text Logo" />
        <nav class="menu">
          <button @click="navigateTo('map')" :class="{ active: activeMenu === 'map' }">Объявления</button>
          <button @click="navigateTo('tips')" :class="{ active: activeMenu === 'tips' }">Полезные советы</button>
          <button @click="navigateTo('contacts')" :class="{ active: activeMenu === 'contacts' }">Контакты</button>
        </nav>
      </div>
      <div class="header-actions">
        <button class="btn-primary" @click="handleCreateAd">Create Ad</button>
        <el-button icon="el-icon-user" @click="handleUserClick" circle></el-button>
        <button class="chat-toggle" @click="toggleChat">
          <img src="@/assets/msg_icon.svg" alt="Chat Icon" />
        </button>
      </div>
    </header>
    <main class="content">
      <router-view :isChatOpen="isChatOpen" @toggleChat="toggleChat"></router-view>
    </main>
  </div>
</template>

<script>
import { ElButton } from 'element-plus';

export default {
  name: 'MainLayout',
  components: {
    ElButton,
  },
  data() {
    return {
      activeMenu: 'map',
      isChatOpen: false  // Data property to control chat visibility
    };
  },
  methods: {
    navigateTo(section) {
      this.activeMenu = section;
      this.$router.push(`/${section}`);
    },
    handleCreateAd() {
      // Логика для создания объявления
    },
    handleUserClick() {
      // Логика для меню пользователя
    },
    toggleChat() {
      this.isChatOpen = !this.isChatOpen; // Toggle chat window visibility
    }
  }
};
</script>
<style scoped>
/* Основной стиль для логотипа */
.logo {
  padding-right: 20px;
}

/* Основной контейнер */
.main-layout {
  display: flex;
  flex-direction: column;
  height: 100%;
  margin-top: 37px;
}

/* Хедер */
.header {
  position: fixed;
  top: 0;
  left: 0;
  width: 90vw;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 5%;
  border-bottom: 1px solid #e6e6e6;
  background-color: #ffffff;
  z-index: 1000;
}

/* Левая часть хедера: логотип и меню */
.header-left {
  display: flex;
  align-items: center;
}

.menu {
  display: flex;
  gap: 20px;
}

.menu button {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 13px;
  font-family: ubuntu;
  color: #898989;
  position: relative;
  padding: 10px 10px;
  transition: all 0.3s ease;
}

.menu button::after {
  content: '';
  position: absolute;
  left: 0;
  bottom: 0;
  width: 0;
  height: 2px;
  transition: width 0.3s ease;
}

.menu button:hover::after {
  width: 100%;
}

.menu button.active {
  border-radius: 4px;
  font-weight: 1000;
  color: rgb(0, 0, 0);
}

/* Кнопки действий */
.header-actions {
  display: flex;
  align-items: center;
  gap: 10px;
}

.btn-primary {
  padding: 5px 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.btn-primary:hover {
  background-color: #0056b3;
}

/* Кнопка чата */
.chat-toggle {
  background: none;
  border: none;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.chat-toggle:hover {
  background-color: #f0f0f0;
}

.chat-toggle img {
  width: 20px;
  height: 20px;
}

/* Окно чата */
.chat-window {
  position: fixed;
  bottom: 0;
  right: 0;
  width: 300px;
  height: 400px;
  background-color: #ffffff;
  border: 1px solid #e6e6e6;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  z-index: 1001;
}
</style>

