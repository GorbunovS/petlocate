import { createRouter, createWebHistory } from 'vue-router'
import LoginPage from '../components/LoginPage.vue'
import MainLayout from '../components/MainLayout.vue';
import ContactPage from '../components/ContactPage.vue'; 
import MapLayout from '../components/MapLayout.vue';
const routes = [
  { path: '/login', component: LoginPage },
  { path: '/',
    component: MainLayout,
    children: [
      { path: 'map', component: MapLayout },
      { path: 'contacts', component: ContactPage },
      { path: '', redirect: 'map' } 
    ]
  }
];
const router = createRouter({
  history: createWebHistory(),
  routes
})
export default router
