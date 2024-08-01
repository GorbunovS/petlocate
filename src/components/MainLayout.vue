<template>
  <div class="main-layout">
    <el-header class="header">
      <div class="logo">Logo</div>
      <el-menu :default-active="activeMenu" class="menu" @select="handleMenuSelect" mode="horizontal">
        <el-menu-item index="map">Map</el-menu-item>
        <el-menu-item index="board">Bulletin Board</el-menu-item>
        <el-menu-item index="tips">Tips</el-menu-item>
        <el-menu-item index="contacts">Contacts</el-menu-item>
      </el-menu>
      <div class="header-actions">
        <el-button type="primary" @click="handleCreateAd">Create Ad</el-button>
        <el-button icon="el-icon-user" @click="handleUserClick"></el-button>
      </div>
    </el-header>
    <el-main class="content">
      <router-view></router-view>
    </el-main>
    <el-footer class="footer">
      <p>Site information and footer content</p>
    </el-footer>
  </div>
</template>

<script>
import { ElHeader, ElMain, ElFooter, ElMenu, ElMenuItem, ElButton } from 'element-plus';

export default {
  components: {
    ElHeader,
    ElMain,
    ElFooter,
    ElMenu,
    ElMenuItem,
    ElButton
  },
  name: 'MainLayout',
  data() {
    return {
      activeMenu: 'map'
    };
  },
  methods: {
    handleMenuSelect(index) {
      this.activeMenu = index;
      this.$router.push(`/${index}`); // Перенаправление на соответствующий маршрут
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

.main-layout {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.header {
  position: fixed; /* Make header fixed */
  top: 0;
  left: 0;
  width: 100%; /* Full width */
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  background-color: #f5f5f5;
  z-index: 1000; /* Ensure header is above other content */
}

.menu {
  flex: 1;
  margin: 0 20px;
}

.header-actions {
  display: flex;
  align-items: center;
}

.content {
  flex: 1;
  width: 100%;
  height: 100%;
  margin-top: 50px; 
  display: flex;
  justify-content: center;
  align-items: center;
}
.el-main {
  --el-main-padding: 0px;
}

.el-header {
  --el-header-padding: 0px;
}
.footer {
  padding: 10px;
  background-color: #f5f5f5;
}
</style>
