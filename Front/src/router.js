import { createRouter, createWebHistory } from 'vue-router'
import Home from './pages/Home.vue'
import About from './pages/About.vue'
import Login from './pages/Login.vue'
import Products from './components/Products.vue'
import FAQ from './pages/FAQ.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/about', component: About },
  { path: '/login', component: Login },
  { path: '/products', component: Products },
  { path: '/duvidas', component: FAQ },
  
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
