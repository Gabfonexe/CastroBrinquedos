<template>
  <div class="app-container">
  <Toast />

    <MenuBar class="navbar" />

    <section class="hero-section">
      <div class="container text-center">
        <h1 class="hero-title">Castro Brinquedos</h1>
        <p class="hero-subtitle">Transforme sua festa em um parque de diversão!</p>
        <Button label="Ver Brinquedos" class="cta-button" @click="scrollToSection('products')" />
      </div>
    </section>

    <section class="products-section" ref="products">
  <div class="container">
    <h2 class="section-title">Nossos Brinquedos</h2>
    <Carousel :value="products" :numVisible="3" :numScroll="1" :responsiveOptions="responsiveOptions">
      <template #item="slotProps">
        <div class="border border-surface-200 dark:border-surface-700 rounded m-2 p-4">
          <div class="mb-4">
            <div class="relative mx-auto">
              <img :src="slotProps.data.image" :alt="slotProps.data.name" class="w-full rounded" style="height: 200px; object-fit: cover;" />
            </div>
          </div>
          <div class="mb-2 font-medium text-lg text-center">{{ slotProps.data.name }}</div>
          <div class="text-center mb-2 text-sm">{{ slotProps.data.description }}</div>
          <div class="flex justify-center font-semibold text-xl text-red-500">
            R$ {{ slotProps.data.price }}/dia
            <Button
                :icon="isProductSelected(slotProps.data) ? 'pi pi-check' : 'pi pi-plus'"
                @click="toggleItem(slotProps.data)"
                :class="['transition-all', isProductSelected(slotProps.data) ? 'bg-white text-green-600 border border-green-500'  : 'bg-green-500 text-white']"
              />
          </div>  
        </div>
      </template>
    </Carousel>
  </div>
</section>

    <section class="calendar-section">
      <div class="container text-center">
        <h2 class="section-title">Disponibilidade</h2>
        <Calendar 
          v-model="selectedDate"
          :inline="true"
          :minDate="minDate"
          :maxDate="maxDate"
          :disabledDates="disabledDates"
          class="responsive-calendar"
        />
      </div>
    </section>

    <section class="contact-section">
      <div class="container text-center">
        <h2 class="section-title">Entre em Contato</h2>
        <p>Solicite um orçamento personalizado para sua festa!</p>
        <Button label="Fale Conosco" @click="showContactDialog = true" class="contact-button" />
      </div>
    </section>

    <footer class="footer">
      <div class="container text-center">
        <p>Castro Brinquedos &copy; {{ new Date().getFullYear() }}</p>
      </div>
    </footer>

    <Dialog v-model:visible="showContactDialog" modal header="Contato" :style="{ width: '90vw', maxWidth: '500px' }">
      <div class="contact-form">
        <div class="form-group">
          <label for="name">Nome</label>
          <InputText id="name" v-model="contactForm.name" class="form-control" />
        </div>
        <div class="form-group">
          <label for="email">Email</label>
          <InputText id="email" v-model="contactForm.email" class="form-control" />
        </div>
        <div class="form-group">
          <label for="phone">Celular</label>
          <InputText id="phone" v-model="contactForm.phone" class="form-control" />
        </div>
        <div class="form-group">
          <label for="message">Mensagem</label>
          <Textarea id="message" v-model="contactForm.message" rows="3" class="form-control" />
        </div>
      </div>
      <template #footer>
        <Button label="Cancelar" @click="showContactDialog = false" class="p-button-text" />
        <Button label="Enviar" @click="submitContactForm" />
      </template>
    </Dialog>
  </div>
</template>

<script>
import Calendar from 'primevue/calendar';
import Dialog from 'primevue/dialog';
import Button from 'primevue/button';
import InputText from 'primevue/inputtext';
import Textarea from 'primevue/textarea';
import Card from 'primevue/card';
import MenuBar from './components/MenuBar.vue';
import Carousel from 'primevue/carousel';
import axios from 'axios';
import Toast from 'primevue/toast';
import ToggleButton from 'primevue/togglebutton';

export default {
  name: 'App',
  components: {
    Calendar,
    Dialog,
    Button,
    InputText,
    Textarea,
    Card,
    MenuBar,
    Carousel,
    Toast,
    ToggleButton
  },
  data() {
    const today = new Date();
    const nextYear = new Date();
    nextYear.setFullYear(today.getFullYear() + 1);

    return {
      selectedProducts: [],
      amount: 0,
      showContactDialog: false,
      selectedDate: null,
      minDate: today,
      maxDate: nextYear,
      isSelected: false,
      disabledDates: [
        new Date(2025, 11, 25),
        new Date(2025, 11, 31),
        new Date(2025, 10, 15),
      ],
      contactForm: {
        name: '',
        email: '',
        phone: '',
        message: '',
      },
      products: [
        {
          id: 1,
          name: 'Pula-Pula',
          description: 'Pula-pula grande para crianças de até 12 anos',
          price: 150,
          image: 'src/assets/pula_pula.jpg'
        },
        {
          id: 2,
          name: 'Piscina de Bolinhas',
          description: '2x2m com 5000 bolinhas',
          price: 120,
          image: 'src/assets/piscina_bolinha.jpg'
        },
        {
          id: 3,
          name: 'Castelo Inflável',
          description: 'Com escorregador, 3m de altura',
          price: 200,
          image: 'src/assets/toboga.jpg'
        },
        {
          id: 4,
          name: 'Castelo Inflável',
          description: 'Com escorregador, 3m de altura',
          price: 200,
          image: 'https://example.com/castelo.jpg'
        },
        {
          id: 5,
          name: 'Castelo Inflável',
          description: 'Com escorregador, 3m de altura',
          price: 200,
          image: 'https://example.com/castelo.jpg'
        },
        {
          id: 6,
          name: 'Castelo Inflável',
          description: 'Com escorregador, 3m de altura',
          price: 200,
          image: 'https://example.com/castelo.jpg'
        },
        {
          id: 7,
          name: 'Castelo Inflável',
          description: 'Com escorregador, 3m de altura',
          price: 200,
          image: 'https://example.com/castelo.jpg'
        },
        {
          id: 8,
          name: 'Castelo Inflável',
          description: 'Com escorregador, 3m de altura',
          price: 200,
          image: 'https://example.com/castelo.jpg'
        },
        {
          id: 9,
          name: 'Castelo Inflável',
          description: 'Com escorregador, 3m de altura',
          price: 200,
          image: 'https://example.com/castelo.jpg'
        },
      ]
    };
  },
  methods: {
    toggleItem(product) {
      const index = this.selectedProducts.findIndex(p => p.id === product.id);
      if (index > -1) {
        this.selectedProducts.splice(index, 1); // já estava selecionado, remove
      } else {
        this.selectedProducts.push(product); // adiciona o produto selecionado
      }
    },

    isProductSelected(product) {
      return this.selectedProducts.some(p => p.id === product.id);
    },
    sendUserData(){
      
    },
    submitContactForm() {
      this.amount = this.selectedProducts.reduce((total, produto) => total + produto.price, 0);
      const userData = {name:this.contactForm.name, email:this.contactForm.email, phone:this.contactForm.phone, message:this.contactForm.message, date:this.selectedDate, amount:this.amount};
      axios.post('http://localhost:8080/criar',userData)

      this.contactForm = {
        name: '',
        email: '',
        phone: '',
        message: '',
      };

      this.showContactDialog = false;

      this.$toast.add({
        severity: 'success',
        summary: 'Sucesso',
        detail: 'Seu cadastro foi realizado com sucesso, em breve entraremos em contato!',
        life: 2000,
      })
      
    },
    scrollToSection(refName) {
      const section = this.$refs[refName];
      if (section) section.scrollIntoView({ behavior: 'smooth' });
    }
  },
  computed: {
  totalAmount() {
  
  }
}
};
</script>

<style>
:root {
  --primary-color: #007BFF; /* Azul */
  --secondary-color: #FF4136; /* Vermelho */
  --accent-color: #FFD700; /* Amarelo */
  --bg-light: #f9f9f9;
  --text-color: #333;
}

body {
  font-family: 'Roboto', sans-serif;
  margin: 0;
  background-color: var(--bg-light);
  color: var(--text-color);
}

.container {
  width: 90%;
  max-width: 1200px;
  margin: auto;
}

/* Navbar */
.navbar {
  background-color: var(--primary-color);
  color: white;
  padding: 1rem;
}

/* Hero */
.hero-section {
  background: linear-gradient(to right, var(--primary-color), var(--secondary-color));
  color: white;
  padding: 4rem 1rem;
  text-align: center;
}

.hero-title {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.hero-subtitle {
  font-size: 1.5rem;
  margin-bottom: 2rem;
}

.cta-button {
  background-color: var(--accent-color);
  border: none;
  font-size: 1.1rem;
  padding: 0.75rem 2rem;
}

/* Products */
.products-section {
  padding: 4rem 1rem;
}

.section-title {
  font-size: 2.5rem;
  color: var(--primary-color);
  margin-bottom: 2rem;
  text-align: center;
}

.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
}

.product-card {
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 6px 12px rgba(0,0,0,0.1);
  transition: transform 0.3s;
}

.product-card:hover {
  transform: translateY(-5px);
}

.product-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.price {
  font-weight: bold;
  color: var(--secondary-color);
  font-size: 1.2rem;
  margin-top: 1rem;
}

/* Calendar */
.calendar-section {
  background-color: white;
  padding: 4rem 1rem;
}

/* Contact */
.contact-section {
  background-color: var(--accent-color);
  color: #000;
  padding: 4rem 1rem;
}

.contact-button {
  background-color: var(--secondary-color);
  color: white;
  border: none;
  margin-top: 1rem;
  font-size: 1rem;
  padding: 0.75rem 1.5rem;
}

/* Footer */
.footer {
  background-color: var(--primary-color);
  color: white;
  padding: 2rem 1rem;
  text-align: center;
}

/* Form */
.contact-form {
  display: grid;
  gap: 1rem;
}

.form-group {
  display: flex;
  flex-direction: column;
}

.form-control {
  padding: 0.5rem;
  border-radius: 4px;
  border: 1px solid #ccc;
}

@media (max-width: 768px) {
  .hero-title {
    font-size: 2rem;
  }
  .section-title {
    font-size: 2rem;
  }
}
</style>
