<template>
  <header class="bg-white dark:bg-gray-900 shadow-md rounded-2xl px-6 py-4 mb-6 transition-colors duration-300">
    <div class="flex items-center justify-between" id="inicio">

      <img src="/src/assets/logo_castro.png" alt="Logo" class="w-40 sm:w-44 transition-all duration-300 animate-pulse " />

      <nav class="hidden sm:flex gap-8 items-center text-transparent bg-clip-text bg-gradient-to-r from-red-400 to-blue-600 text-xl font-bold p-1  animate-pulse">
        <template v-for="item in menuItems" :key="item.label">
          <a
            v-if="item.url"
            :href="item.url"
            target="_blank"
            rel="noopener noreferrer"
            class="flex items-center gap-2 hover:text-blue-600 transition-colors duration-300"
          >
            <i :class="item.icon" v-if="item.icon"></i>
            {{ item.label }}
          </a>
          <button
            v-else
            @click="item.command"
            class="flex items-center gap-2 hover:text-blue-600 transition-colors duration-300"
          >
            <i :class="item.icon" v-if="item.icon"></i>
            {{ item.label }}
          </button>
        </template>
      </nav>

      
      <button
        class="sm:hidden text-transparent bg-clip-text bg-gradient-to-r from-red-400 to-blue-600 text-xl font-bold p-1"
        @click="toggleMobileMenu"
      >
        <i class="pi pi-bars text-2xl"></i>
      </button>
    </div>

    <transition name="fade" mode="out-in">
      <div
        v-if="mobileMenuOpen"
        class="sm:hidden mt-4 space-y-3 animate-slide-down"
      >
        <template v-for="item in menuItems" :key="item.label">
          <a
            v-if="item.url"
            :href="item.url"
            target="_blank"
            rel="noopener noreferrer"
            class="block px-2 py-2 rounded-md text-transparent bg-clip-text bg-gradient-to-r from-red-400 to-blue-600 text-xl font-bold p-1  animate-pulse"
          >
            <i :class="item.icon" v-if="item.icon"></i>
            {{ item.label }}
          </a>
          <button
            v-else
            @click="item.command"
            class="block w-full text-left px-2 py-2 rounded-md text-gray-800 dark:text-gray-200 hover:bg-blue-100 dark:hover:bg-gray-800 transition-colors"
          >
            <i :class="item.icon" v-if="item.icon"></i>
            {{ item.label }}
          </button>
        </template>
      </div>
    </transition>
  </header>
</template>

<script>
import Menubar from 'primevue/menubar';
import Button from 'primevue/button';

export default {
  name: 'MenuTopBar',
  components: {
    Menubar,
    Button,
  },
  data() {
    return {
      mobileMenuOpen: false,
      showContactDialog: false,
      menuItems: [
        {
          label: 'WhatsApp',
          icon: 'pi pi-whatsapp',
          url: 'https://wa.me/5521968843651',
        },
        {
          label: 'Instagram',
          icon: 'pi pi-instagram',
          url: 'https://instagram.com/castrobrinquedos',
        },
        {
          label: 'Home',
          icon: 'pi pi-home',
          url: 'https://castro-brinquedos.vercel.app/',
        },
      ],
    };
  },
  methods: {
    scrollToSection(refName) {
      const section = this.$refs[refName];
      if (section) {
        section.scrollIntoView({ behavior: 'smooth' });
      }
    },
    toggleMobileMenu() {
      this.mobileMenuOpen = !this.mobileMenuOpen;
    },
  },
};
</script>

<style scoped>
/* Animação de deslizamento para baixo no menu mobile */
@keyframes slideDown {
  0% {
    opacity: 0;
    transform: translateY(-10px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}
.animate-slide-down {
  animation: slideDown 0.3s ease-out forwards;
}
</style>