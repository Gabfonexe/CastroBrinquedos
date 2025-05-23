<template>
  <header class="bg-white dark:bg-gray-900 shadow-md rounded-2xl p-4 mb-6">
    <div class="flex items-center justify-between">
      <!-- Logo -->
      <img src="/src/assets/logo_castro.png" alt="Logo" class="w-44" />

      <!-- Navegação Desktop -->
      <nav class="hidden sm:flex gap-6 text-gray-800 dark:text-gray-200 font-semibold items-center">
        <template v-for="item in menuItems" :key="item.label">
          <a
            v-if="item.url"
            :href="item.url"
            target="_blank"
            rel="noopener noreferrer"
            class="hover:text-blue-600 transition-colors duration-200 flex items-center gap-1"
          >
            <i :class="item.icon" v-if="item.icon"></i> {{ item.label }}
          </a>
          <button
            v-else
            @click="item.command"
            class="hover:text-blue-600 transition-colors duration-200 flex items-center gap-1"
          >
            <i :class="item.icon" v-if="item.icon"></i> {{ item.label }}
          </button>
        </template>
      </nav>

      <!-- Botão mobile -->
      <Button
        icon="pi pi-bars"
        class="sm:hidden p-button-rounded p-button-text text-gray-700 dark:text-gray-300 hover:text-blue-500"
        @click="toggleMobileMenu"
      />
    </div>

    <!-- Navegação Mobile -->
    <transition name="fade">
      <div v-if="mobileMenuOpen" class="sm:hidden mt-4 space-y-3">
        <template v-for="item in menuItems" :key="item.label">
          <a
            v-if="item.url"
            :href="item.url"
            target="_blank"
            rel="noopener noreferrer"
            class="block text-gray-800 dark:text-gray-200 hover:text-blue-600 transition-colors"
          >
            <i :class="item.icon" v-if="item.icon"></i> {{ item.label }}
          </a>
          <button
            v-else
            @click="item.command"
            class="block w-full text-left text-gray-800 dark:text-gray-200 hover:text-blue-600 transition-colors"
          >
            <i :class="item.icon" v-if="item.icon"></i> {{ item.label }}
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
          label: 'Início',
          command: () => this.scrollToSection('products'),
        },
        {
          label: 'Contato',
          command: () => (this.showContactDialog = true),
        },
        {
          label: 'WhatsApp',
          icon: 'pi pi-whatsapp',
          url: 'https://wa.me/55000000000',
        },
        {
          label: 'Instagram',
          icon: 'pi pi-instagram',
          url: 'https://instagram.com/castrobrinquedos',
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
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
