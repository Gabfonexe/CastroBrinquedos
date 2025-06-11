import { createApp } from 'vue'
import { createPinia } from 'pinia'
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
import Aura from '@primeuix/themes/aura';
import Tooltip from 'primevue/tooltip';



import 'primevue/resources/themes/lara-light-blue/theme.css'
import 'primevue/resources/primevue.min.css'
import 'primeicons/primeicons.css'
import 'primeflex/primeflex.css';

const pt = {
            firstDayOfWeek: 0,
            dayNames: ["domingo", "segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado"],
            dayNamesShort: ["dom", "seg", "ter", "qua", "qui", "sex", "sáb"],
            dayNamesMin: ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sab"],
            monthNames: ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"],
            monthNamesShort: ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"],
            today: "Hoje",
            clear: "Limpar",
            dateFormat: "dd/mm/yy",
            weekHeader: "Sm"
          };

const app = createApp(App)
app.use(createPinia())
app.use(router)
app.use(PrimeVue, {
    locale: pt,
    theme: {
        preset: Aura,
        options: {
            cssLayer: {
                name: 'primevue',
                order: 'tailwind-base, primevue, tailwind-utilities'
            }
        }
    }
});
app.use(ToastService)
app.component('Toast', Toast)

app.component('p-input-text', InputText)
app.component('p-password', Password)
app.component('p-button', Button)
app.directive('tooltip', Tooltip);
app.directive('ripple', Ripple)
app.component('Menu', Menu)

app.mount('#app')
