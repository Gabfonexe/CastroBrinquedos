<template>
  <div class="app-container">
    <Toast />
    <Menubar :model="menuItems" class="mb-4 shadow-2 surface-card" />

    <div class="flex justify-end px-4">
      <Button icon="pi pi-moon" class="p-button-text" @click="toggleTheme" />
    </div>

    <section class="hero-section text-center py-8 px-4 surface-ground">
      <h1 class="text-5xl font-bold text-primary mb-3">Castro Brinquedos</h1>
      <p class="text-lg text-color-secondary mb-4">Transforme sua festa em um parque de diversão!</p>
      <Button label="Ver Brinquedos" class="p-button-raised p-button-rounded p-button-warning" @click="scrollToSection('products')" />
    </section>

    <section class="products-section py-8 px-4" ref="products">
      <h2 class="text-3xl text-center text-primary mb-6">Nossos Brinquedos</h2>
      <Carousel :value="products" :numVisible="3" :numScroll="1" :responsiveOptions="responsiveOptions">
        <template #item="slotProps">
          <Card class="m-2 shadow-2">
            <template #header>
              <img :src="slotProps.data.image" :alt="slotProps.data.name" class="w-full h-48 object-cover rounded-t" />
            </template>
            <template #title>
              <div class="text-center font-bold">{{ slotProps.data.name }}</div>
            </template>
            <template #content>
              <p class="text-sm text-center">{{ slotProps.data.description }}</p>
              <div class="text-center mt-2 font-semibold text-xl text-red-500">
                R$ {{ slotProps.data.price }}/dia
              </div>
            </template>
            <template #footer>
              <div class="flex justify-center">
                <Button
                  :icon="isProductSelected(slotProps.data) ? 'pi pi-check' : 'pi pi-plus'"
                  @click="toggleItem(slotProps.data)"
                  :class="[isProductSelected(slotProps.data) ? 'p-button-outlined p-button-success' : 'p-button-success']"
                  class="mt-2"
                />
              </div>
            </template>
          </Card>
        </template>
      </Carousel>
    </section>

    <section class="calendar-section py-8 px-4 surface-50">
      <h2 class="text-3xl text-center text-primary mb-4">Disponibilidade</h2>
      <div class="flex justify-center">
        <Calendar
          v-model="selectedDate"
          :inline="true"
          :minDate="minDate"
          :maxDate="maxDate"
          :disabledDates="disabledDates"
          class="p-calendar"
        />
      </div>
    </section>

    <section class="contact-section py-8 px-4 bg-yellow-100">
      <h2 class="text-3xl text-center text-primary mb-3">Entre em Contato</h2>
      <p class="text-center mb-4">Solicite um orçamento personalizado para sua festa!</p>
      <div class="flex justify-center">
        <Button label="Fale Conosco" class="p-button-rounded p-button-danger" @click="showContactDialog = true" />
      </div>
    </section>

    <section class="testimonials-section py-8 px-4 surface-ground">
      <h2 class="text-3xl text-center text-primary mb-6">O que nossos clientes dizem</h2>
      <div class="grid md:grid-cols-3 gap-4">
        <Card v-for="testimonial in testimonials" :key="testimonial.name" class="shadow-2 border-round-xl p-4 transition-all hover:shadow-4">
          <template #content>
            <p class="italic mb-3">"{{ testimonial.message }}"</p>
            <div class="text-right font-semibold text-primary">— {{ testimonial.name }}</div>
          </template>
        </Card>
      </div>
    </section>

    <section class="faq-section py-8 px-4 bg-yellow-50">
      <h2 class="text-3xl text-center text-primary mb-6">Perguntas Frequentes</h2>
      <Accordion :multiple="true" :activeIndex="[0]">
        <AccordionTab v-for="(faq, index) in faqs" :key="index" :header="faq.question">
          <p>{{ faq.answer }}</p>
        </AccordionTab>
      </Accordion>
    </section>

    <footer class="footer bg-primary text-white text-center py-4">
      <p>Castro Brinquedos &copy; {{ new Date().getFullYear() }}</p>
    </footer>

    <Dialog v-model:visible="showContactDialog" modal header="Contato" :style="{ width: '90vw', maxWidth: '500px' }">
      <div class="p-fluid">
        <div class="field">
          <label for="name">Nome</label>
          <InputText id="name" v-model="contactForm.name" />
        </div>
        <div class="field">
          <label for="email">Email</label>
          <InputText id="email" v-model="contactForm.email" />
        </div>
        <div class="field">
          <label for="phone">Celular</label>
          <InputText id="phone" v-model="contactForm.phone" />
        </div>
        <div class="field">
          <label for="message">Mensagem</label>
          <Textarea id="message" v-model="contactForm.message" rows="3" />
        </div>
      </div>
      <template #footer>
        <Button label="Cancelar" class="p-button-text" @click="showContactDialog = false" />
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
import Carousel from 'primevue/carousel';
import Toast from 'primevue/toast';
import Menubar from 'primevue/menubar';
import Accordion from 'primevue/accordion';
import AccordionTab from 'primevue/accordiontab';
import axios from 'axios';

export default {
  name: 'App',
  components: {
    Calendar,
    Dialog,
    Button,
    InputText,
    Textarea,
    Card,
    Carousel,
    Toast,
    Menubar,
    Accordion,
    AccordionTab
  },
  data() {
    const today = new Date();
    const nextYear = new Date();
    nextYear.setFullYear(today.getFullYear() + 1);

    return {
      showContactDialog: false,
      selectedDate: null,
      minDate: today,
      maxDate: nextYear,
      contactForm: {
        name: '',
        email: '',
        phone: '',
        message: '',
      },
      disabledDates: [
        new Date(2025, 11, 25),
        new Date(2025, 11, 31),
        new Date(2025, 10, 15),
      ],
      selectedProducts: [],
      products: [
        { id: 1, name: 'Pula-Pula', description: 'Pula-pula grande para crianças de até 12 anos', price: 150, image: 'src/assets/pula_pula.jpg' },
        { id: 2, name: 'Piscina de Bolinhas', description: '2x2m com 5000 bolinhas', price: 120, image: 'src/assets/piscina_bolinha.jpg' },
        { id: 3, name: 'Castelo Inflável', description: 'Com escorregador, 3m de altura', price: 200, image: 'src/assets/toboga.jpg' },
        { id: 4, name: 'Castelo Inflável', description: 'Com escorregador, 3m de altura', price: 200, image: 'https://example.com/castelo.jpg' },
      ],
      testimonials: [
        { name: 'Joana Silva', message: 'Excelente serviço! As crianças se divertiram demais.' },
        { name: 'Carlos Mendes', message: 'Ótima qualidade dos brinquedos e atendimento muito atencioso.' },
        { name: 'Ana Paula', message: 'Tudo chegou no horário e foi super tranquilo. Recomendo!' },
      ],
      faqs: [
        { question: 'Com quanto tempo de antecedência preciso reservar?', answer: 'Recomendamos pelo menos 1 semana antes do evento para garantir a disponibilidade.' },
        { question: 'O transporte está incluso no valor?', answer: 'Sim, para eventos dentro da cidade. Fora da cidade pode haver taxa adicional.' },
        { question: 'Como faço o pagamento?', answer: 'Aceitamos PIX, transferência bancária e cartão de crédito.' },
      ],
      menuItems: [
        { label: 'Início', command: () => this.scrollToSection('products') },
        { label: 'Contato', command: () => (this.showContactDialog = true) },
        { label: 'WhatsApp', icon: 'pi pi-whatsapp', url: 'https://wa.me/55000000000' },
        { label: 'Instagram', icon: 'pi pi-instagram', url: 'https://instagram.com/castrobrinquedos' }
      ],
      isDark: false,
    };
  },
  methods: {
    scrollToSection(refName) {
      const section = this.$refs[refName];
      if (section) section.scrollIntoView({ behavior: 'smooth' });
    },
    toggleItem(product) {
      const index = this.selectedProducts.findIndex(p => p.id === product.id);
      if (index > -1) this.selectedProducts.splice(index, 1);
      else this.selectedProducts.push(product);
    },
    isProductSelected(product) {
      return this.selectedProducts.some(p => p.id === product.id);
    },
    toggleTheme() {
      this.isDark = !this.isDark;
      document.body.classList.toggle('p-component-overlay-dark', this.isDark);
      document.body.classList.toggle('dark', this.isDark);
    },
    submitContactForm() {
      const amount = this.selectedProducts.reduce((total, produto) => total + produto.price, 0);
      const userData = {
        ...this.contactForm,
        date: this.selectedDate,
        amount
      };
      axios.post('http://localhost:8080/criar', userData);
      this.contactForm = { name: '', email: '', phone: '', message: '' };
      this.showContactDialog = false;
      this.$toast.add({
        severity: 'success',
        summary: 'Sucesso',
        detail: 'Seu cadastro foi realizado com sucesso!',
        life: 3000
      });
    }
  }
};
</script>

<style>
body.dark {
  background-color: #1e1e1e;
  color: #f0f0f0;
}
.card,
.p-accordion-tab {
  transition: all 0.3s ease;
}
</style>
