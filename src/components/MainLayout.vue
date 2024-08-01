<template>
  <div class="main-layout">
    <header class="header">
      <img class="logo" src="@/assets/text-logo.svg" alt="Text Logo" />
      <nav class="menu">
        <button @click="navigateTo('map')" :class="{ active: activeMenu === 'map' }">Объявления</button>
        <button @click="navigateTo('tips')" :class="{ active: activeMenu === 'tips' }">Полезные советы</button>
        <button @click="navigateTo('contacts')" :class="{ active: activeMenu === 'contacts' }">Контакты</button>
      </nav>
      <div class="header-actions">
        <button class="btn-primary" @click="handleCreateAd">Create Ad</button>
        <button class="btn-user" @click="handleUserClick">User</button>
      </div>
    </header>
    <main class="content">
      <router-view></router-view>
    </main>
    <!-- <footer class="footer">
      <p>Site information and footer content</p>
    </footer> -->
  </div>
</template>

<script>
export default {
  name: 'MainLayout',
  data() {
    return {
      activeMenu: 'map'
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
    }
  }
};
</script>

<style scoped>
/* Основной стиль для логотипа */
.logo {
  background-color: white;
  padding: 0 100px;
}

/* Основной контейнер */
.main-layout {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

/* Хедер */
.header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  background-color: #ffffff;
  z-index: 1000;
}

/* Меню */
.menu {
  display: flex;
  gap: 20px;
}

.menu button {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 16px;
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
  background-color: #835DF0;
  transition: width 0.3s ease;
}

.menu button:hover::after {
  width: 100%;
}


.menu button.active {
  background-color: #6f4fb0;
  border-radius: 4px;
  color: white;
  
}

/* Кнопки действий */
.header-actions {
  display: flex;
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

.btn-user {
  padding: 5px;
  background: none;
  border: none;
  cursor: pointer;
  font-size: 16px;
}

/* Контент */
.content {
  flex: 1;
  margin-top: 0px; /* Учитываем высоту фиксированного хедера */
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 20%;
}

</style>
