import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import PrimeVue from 'primevue/config'
import InputText from 'primevue/inputtext'
import Password from 'primevue/password'
import Button from 'primevue/button'
import Menu from 'primevue/menu'
import Ripple from 'primevue/ripple'
import Toast from 'primevue/toast'
import ToastService from 'primevue/toastservice'

import 'primevue/resources/themes/lara-light-blue/theme.css'
import 'primevue/resources/primevue.min.css'
import 'primeicons/primeicons.css'
import 'primeflex/primeflex.css';

const app = createApp(App)

app.use(router)
app.use(PrimeVue)
app.use(ToastService)
app.component('Toast', Toast)

app.component('p-input-text', InputText)
app.component('p-password', Password)
app.component('p-button', Button)
app.directive('ripple', Ripple)
app.component('Menu', Menu)

app.mount('#app')
