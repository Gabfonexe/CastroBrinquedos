import { createRouter, createWebHistory } from 'vue-router'
import app from './app.vue'


const routes = [
  { path: '/', component: app },


]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
